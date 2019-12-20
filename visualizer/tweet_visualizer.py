from matplotlib import pyplot as plt
import pandas as pd

from analyzer.twitter_analyzer import *

class TweetVisualizer:
    def __init__(self, dataframe, index, legend=None, figsize=(25,5)):
        self.dataframe = dataframe
        self.index = dataframe[index]
        self.legend = legend
        self.figsize = figsize

    def show(self):
        plt.show()

    def add_to_figure(self, data):
        time_data = pd.Series(data=self.dataframe[str(data)].values, index=self.index)
        if (self.legend == None):
            time_data.plot(figsize=self.figsize.value)
        else:
            time_data.plot(figsize=self.figsize, label=str(data), legend=self.legend)

    def draw_single(self, data, color):
        time_data = pd.Series(data=self.dataframe[str(data)].values, index=self.index)
        time_data.plot(figsize=self.figsize, color=color)