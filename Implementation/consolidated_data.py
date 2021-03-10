import pandas as pd
import numpy as np
from ClassRoom import *

pre_test = pd.read_excel("pre_test.xlsx")
pre_survey = pd.read_excel("pre_survey.xlsx")
post_test = pd.read_excel("post_test.xlsx")
post_survey = pd.read_excel("post_survey.xlsx")

def data_for_graph():
    post_test_LO = []
    post_survey_LO = []
    pre_test_LO = []
    pre_survey_LO = []
    consolidated_pre_survey = []    
    consolidated_pre_test = []
    consolidated_post_survey = []
    consolidated_post_test = []
    consolidated_data = []
    data = []
    max_module = module_max()
    min_module = module_min()
    module_average = module_avg()
    data = {}
    for i in range(0, len(pre_survey.columns)):  # iterates throw all the rows
        for j in range(4, 10):  # iterated throw column
            post_test_LO.append(post_test.iloc[i, j])
            post_survey_LO.append(post_survey.iloc[i, j])
            pre_test_LO.append(pre_test.iloc[i, j])
            pre_survey_LO.append(pre_survey.iloc[i, j])
        
        consolidated_pre_survey.append(pre_survey_LO)
        consolidated_pre_survey.append(module_average[0])
        consolidated_pre_survey.append(max_module[0])
        consolidated_pre_survey.append(min_module[0])
        
        consolidated_pre_test.append(pre_test_LO)
        consolidated_pre_test.append(module_average[1])
        consolidated_pre_test.append(max_module[1])
        consolidated_pre_test.append(min_module[1])

        consolidated_post_survey.append(post_survey_LO)
        consolidated_post_survey.append(module_average[2])
        consolidated_post_survey.append(max_module[2])
        consolidated_post_survey.append(min_module[2])

        consolidated_post_test.append(post_test_LO)
        consolidated_post_test.append(module_average[3])
        consolidated_post_test.append(max_module[3])
        consolidated_post_test.append(min_module[3])

        consolidated_data.append(consolidated_pre_survey)
        consolidated_data.append(consolidated_pre_test)
        consolidated_data.append(consolidated_post_survey)
        consolidated_data.append(consolidated_post_test)
        post_test_LO = []
        post_survey_LO = []
        pre_test_LO = []
        pre_survey_LO = []
        data[post_test.iloc[i, 1]] = consolidated_data
        consolidated_data = []
        consolidated_pre_survey = []
        consolidated_pre_test = []
        consolidated_post_survey = []
        consolidated_post_test = []
    return data
