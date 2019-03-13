
import csv

list = [["サナ", "モモ"], ["ナヨン", "ジヒョン"], ["ツウィ", "ジョンヨン"]]

with open("challenge.csv", "w", encoding="UTF-8") as file:
    twice = csv.writer(file, delimiter=",")
    for twice_list in list:
        twice.writerow(twice_list)
        
