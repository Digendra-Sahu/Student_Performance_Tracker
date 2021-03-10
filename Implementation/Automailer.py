import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pretty_html_table import build_table
from email import encoders
from NEW_RADAR import *

pre_survey = pd.read_excel("pre_survey.xlsx")
post_survey = pd.read_excel("post_survey.xlsx")
pre_test = pd.read_excel("pre_test.xlsx")
post_test = pd.read_excel("post_test.xlsx")

pre_test_list1 = []
pre_test_list2 = []
pos_test_list1 = []
pos_test_list2 = []
pre_survey_list1 = []
pre_survey_list2 = []
pos_survey_list1 = []
pos_survey_list2 = []

for i in range(0, len(pre_survey.columns)):
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0

    pre_survey_list1 = pre_test.iloc[i, 4:1en(df.columns)0]
    sum1 = sum(pre_survey_list1)
    pre_survey_list2.append(sum1)

    pos_test_list1 = post_test.iloc[i, 4:10]
    sum2 = sum(pos_test_list1)
    pos_test_list2.append(sum2)

    pre_test_list1 = pre_test.iloc[i, 4:10]
    sum3 = sum(pre_test_list1)
    pre_test_list2.append(sum3)

    pos_survey_list1 = post_survey.iloc[i, 4:10]
    sum4 = sum(pos_survey_list1)
    pos_survey_list2.append(sum4)

arr = np.array(pre_survey_list2)
pre_survey["pre_survey_total"] = arr

arr = np.array(pre_test_list2)
pre_test["pre_test_total"] = arr

arr = np.array(pos_survey_list2)
post_survey["post_survey_total"] = arr

arr = np.array(pos_test_list2)
post_test["post_test_total"] = arr


def maximum():
    maxpresurvey = pre_survey.nlargest(5, ["pre_survey_total"])
    maxpretest = pre_test.nlargest(5, ["pre_test_total"])
    maxpostsurvey = post_survey.nlargest(5, ["post_survey_total"])
    maxpostest = post_test.nlargest(5, ["post_test_total"])

    frames = [maxpresurvey, maxpretest, maxpostsurvey, maxpostest]

    return (pd.concat(frames))

def minimum():
    minpresurvey = pre_survey.nsmallest(3, ["pre_survey_total"])
    minpossurvey = post_survey.nsmallest(3, ["post_survey_total"])
    minpretest = pre_test.nsmallest(3, ["pre_test_total"])
    minpostest = post_test.nsmallest(3, ["post_test_total"])

    frames = [minpresurvey, minpretest, minpossurvey, minpostest]

    return (pd.concat(frames))
