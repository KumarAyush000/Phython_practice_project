class RecursionUtils:
    #Flatten nested list
    """
    def flatten_list(self, matrix):
        matrix = matrix.split("/")
        matrix = [[element.strip() for element in row.split(",")] for row in matrix]
        flat_list = []
        for row in matrix:
            flat_list.extend(row)
        return flat_list
    """
    # even smaller code: 
    def flatten_list(self, matrix):
        return [
                element.strip()
                for row in matrix.split("/")
                for element in row.split(",")
               ]
    