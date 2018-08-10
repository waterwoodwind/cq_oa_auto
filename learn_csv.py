# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 13:06:32 2018

@author: 46979
"""
def get_config_list():
    with open('cq_oa_options.csv','r') as myFile:  
        lines = myFile.readlines()      #读取全部内容 ，并以列表方式返回
        config_list = []
        for line in lines:
            line = line.strip('\n')
            config_list.append(line)
            print(line)
        #删除第一行标题
        company = config_list[0]
        index = company.find(',')
        company = company[:index]
        del(config_list[0])
        del(config_list[0])
    return config_list, company

def get_loc_options_list(config_str):
    index = config_str.find(',')
    loc = config_str[:index]
    options = config_str[index+1:]
    loc_list = loc.split('-')
    options_list = options.split(',')
    return loc_list,options_list


if __name__ == "__main__":
    sentence = "职称状况，成绩状况，基础信息，奖惩通报，员工在岗培养，培训教材，英语培训资料，兼职教员授权信和考官信息，员工服务"
    sentence_list = sentence.split('，')
    c_list, company = get_config_list()