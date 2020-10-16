class MemoryKeeper:
    """
    This is a bit of a weird class, but it can help keep track of information regarding
    what we know about the data points that currently contribute to the graph that is
    presented to the user.

    In essence, it can be made bigger, to keep in memory information on how the graph looks
    and whether whether when callbacks are triggered to update the graph - which parts of it
    need to change. This can optimize the speed at which the information updates and gets
    displayed.

    Currently, this class only holds in memory the time period a table can represent.
    """

    def __init__(self, dataframe, dataframe_name):
        """
        A memory storage that can help get the data updated faster in a graph, when
        call backs are triggered.

        Input:
            dataframe(pd.datafame) - a dataframe from which the information is retrieved
            dataframe_name(str) - a name of the table that is being currently activelly used
                                  in a graph visualization
        """
        import pandas as pd 
        self.time_period = self.setDataframePeriod(new_dataframe=dataframe)
        self.name = self.setName(new_name=dataframe_name)

        # Makrs are generated as indicators to how much of a time period we cover on the graph
        # in gaps of 1 weeks
        self.marks = self.generateMarks()

    def setName(self, new_name):
        """
        Update the name of the table in works

        Input:
            new_name (str) - new table name

        Return:
            A new name. Assign it to the self.name. (TODO: Add additional method to not do this manually)
        """
        return new_name

    def setDataframePeriod(self, new_dataframe):
        """
        Update the period that the dataframe covers.

        Input:
            new_dataframe (pd.DataFrame) - new dataframe for processing

        Return:
            A new range. Assign it to the self.time_period. (TODO: Add additional method to not do this manually)
        """
        return len(new_dataframe.iloc[:,0])

    def generateMarks(self):
        """
        Generate marks that can be displayed on the graph in order to easier locate
        the time frames we are trying to explore.

        Inputs:
            None. All of the information is taken on the presumption that class variables
            have not been altered.

        Return:
            output (dict) - a dictionary with information on what marks should be set on
            the range slider. Save to self.marks if you are calling this manually. 
            (TODO: Add additional method to not do this manually)
        """
        output = {}
        # Go from one, to the maximum amount of days, in steps of 168 (i.e. 168h = 1 week)
        position = 0
        for i in range(1, self.time_period + 1, 168):
            position += 1
            output[i] = f"{position}"
        return output
