from abc import ABC, abstractmethod
import csv
import os

class IBuilder(ABC):
    
    @staticmethod
    @abstractmethod
    def parse(self):
        pass
    
    @staticmethod
    @abstractmethod
    def sum_(self):
        pass
    
    @staticmethod
    @abstractmethod
    def sort(self):
        pass
    
    @staticmethod
    @abstractmethod
    def show_winners(self):
        pass
    
class Score_Builder(IBuilder):
    
    
    """
    raw_merged_files represent all the data merged together it's still messy so we have to unify it.
    merged_files represent the data in a way that we can read it or modify it.
    sorted_data represent the students sorted by their score in ascending order.
    """
    merged_files = {}
    sorted_data = []
    raw_merged_files = []
    
    
    def parse(self):
        """
        This method is to read and append n of csv together.
        """
        for file in os.listdir("./csv_files"):
            if file.endswith(".csv"):
                file = "./csv_files/" + file
                with open(file,encoding="utf8") as file_:
                    reader = csv.DictReader(file_)
                    for row in reader:
                        name = row["First Name"] + " " + row["Last Name"]
                        score = row["Score"]
                        self.raw_merged_files.append([name.lower(), int(score)])
        return self
        
            
    def sum_(self):
        """
        This method sums all the scores of the csv's that have been read by this class.
        """
        for i in self.raw_merged_files:
            if i[0] in self.merged_files:
                self.merged_files[i[0]] += i[1]
            else:
                self.merged_files[i[0]] = i[1]
        return self 
    
    def sort(self,order:bool):
        """
        This method sorts the score of all the students in ascending order to later grab n quantity of students from the top of the list.
        
            Parameters:
                    order (bool) = A boolean that if True sorts in ascending order. False returns the opposite
        """
        for k in sorted(self.merged_files, key=self.merged_files.get, reverse=order):
           r = k, self.merged_files[k]
           self.sorted_data.append(r)
        return self
           
    def show_winners(self, score:int):
        """
        This method shows the first entries of the sorted sum_med scores.
        
            Parameters:
                    n (int) = An integer to select how many winners you want.
        """
          
        try:
            for i in self.sorted_data[0:score]:
                    print(f'--- The students top {score} students are {i[0]}.')
                    print('------------------------------------------------------')
        except:
            print("Error") 
       
    
class Accuracy_Builder(IBuilder):
        
    
    
    # raw_merged_files represent all the data merged together it's still messy so we have to unify it.
    # merged_files represent the data in a way that we can read it or modify it.
    # sorted_data represent the students sorted by their score in ascending order.
    # number_of_files represent the files in the csv files dir, if we keep adding more files the 
    #   :function to get the Accuracy would keep working the way that it is intended.
    
    
    merged_files = {}
    sorted_data = []
    raw_merged_files = []
    number_of_files = []
    
    
    def parse(self):
        """
        This method is to read and append n of csv together.
        """
        for file in os.listdir("./csv_files"):
            if file.endswith(".csv"):
                file = "./csv_files/" + file
                self.number_of_files.append(file)
                with open(file,encoding="utf8") as file_:
                    reader = csv.DictReader(file_)
                    for row in reader:
                        name = row["First Name"] + " " + row["Last Name"]
                        score = row["Accuracy"].replace("%","")
                        self.raw_merged_files.append([name.lower(), int(score)])
        return self
        
    def sum_(self):
        """
        This method sums all the scores of the csv's that have been read by this class.
        """
        for i in self.raw_merged_files:
            if i[0] in self.merged_files:
                self.merged_files[i[0]] += i[1] // len(self.number_of_files)
            else:
                self.merged_files[i[0]] = i[1] // len(self.number_of_files)
        return self 
    
    def sort(self,order:bool):
        """
        This method sorts the score of all the students in ascending order to later grab n quantity of students from the top of the list.
        
            Parameters:
                    order (bool) = A boolean that if True sorts in ascending order, False returns the opposite.
        """
        for k in sorted(self.merged_files, key=self.merged_files.get, reverse=order):
           r = k, self.merged_files[k]
           self.sorted_data.append(r)
        return self
           
    def show_winners(self,score:int):
        """
        This method shows the first entries of the sorted sum_med scores.
        
            Parameters:
                    n (int) = An integer to select the top students based on their accuracy.
        """
        
        try:
            for i in self.sorted_data:
                if i[1] >= score:
                    print(f'--- The students with {score} or more score are {i[0]}. ')
                    print('------------------------------------------------------')
        except:
            print("Error") 

class Director(list):
    
    @classmethod
    def construct(cls):
        return Score_Builder().parse().sum_().sort(True).show_winners(1)
    
    @classmethod
    def constructAccuracy(cls):
        return Accuracy_Builder().parse().sum_().sort(True).show_winners(100)
