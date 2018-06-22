import pandas as pd
import globalparameter, extract_multivalue_feature


def extractall_information(datapath, non_datapath, pos_start_index, pos_end_index, neg_start_index, neg_end_index,
                       column_index_list):
    # extract columns:[4-6,]
    # can not extract column: [7,13,19,25,31,37,43]
    # year column: [49,54,59,64]
    # school column: [46,51,56,61]
    # total column number: 67
    user_data = pd.read_csv(datapath, header=None)
    non_user_data = pd.read_csv(non_datapath, header=None)
    for i in range(len(column_index_list)):
        column_index = column_index_list[i]
        df = pd.concat([user_data.iloc[:, [column_index]],
                        non_user_data.iloc[:, [column_index]]]).values.tolist()
    user_company_data = []
    user_company_data1 = []
    user_company_data_for_dummy = pd.DataFrame()
    # print(df)
    for i in range(len(df)):
        user_company_data.append(' '.join(str(k) for k in df[i]))
    # print(user_skill_data)

    for i in range(len(user_company_data)):
        user_company_data1.append(user_company_data[i].split())
    # print(user_skill_data1)

    user_company_data1 = pd.DataFrame({'companies': user_company_data1})
    # print(user_skill_data1)
    length1 = len(user_company_data1)

    i = 0
    for row in user_company_data1.iterrows():
        user_company_data_for_dummy['user_company' + str(i)] = row[1]
        i = i + 1

    # print(user_company_data_for_dummy)
    company_variable_array = pd.get_dummies(pd.DataFrame(user_company_data1.companies.values.tolist()), drop_first=True)
    new_company_variable_array = pd.concat([company_variable_array.iloc[pos_start_index:pos_end_index],
                                            company_variable_array.iloc[neg_start_index:neg_end_index]])
    new_length = len(new_company_variable_array)
    print(company_variable_array.shape)
    return new_company_variable_array

def bag_of_words_generate_X_train(folderpath, jobtitle, X, ratio):
    # user_profile = pd.DataFrame(pd.read_csv(folderpath + '/test1.csv'))

    # X = user_profile[['normalized_highest_degree', 'normalized_work_year_past1', 'normalized_work_year_past2',
    #                   'normalized_work_year_past3', 'normalized_work_year_past4', 'normalized_work_year_past5',
    #                   'normalized_work_year_past6']]

    # X = X['normalized_highest_degree']

    X = X[['normalized_work_year_past1', 'normalized_work_year_past2',
           'normalized_work_year_past3', 'normalized_work_year_past4', 'normalized_work_year_past5',
           'normalized_work_year_past6']]

    X_train = pd.concat(
        [X.iloc[0:int(globalparameter.extract_number * ratio)], X.iloc[int(globalparameter.extract_number):int(
            globalparameter.extract_number + (globalparameter.total_number - globalparameter.extract_number) * ratio)]])
    bag_of_words_array = extractall_information(folderpath + '/' + 'output_pos_for_dummy.csv',
        folderpath + '/' + 'output_neg_for_dummy.csv', 0,
        int(globalparameter.extract_number * ratio), globalparameter.extract_number,
        globalparameter.extract_number + int((globalparameter.total_number - globalparameter.extract_number) * ratio),)
    skill_dummy_array = extract_multivalue_feature.extractskill(
        folderpath + '/' + 'output_pos_for_dummy.csv',
        folderpath + '/' + 'output_neg_for_dummy.csv', 0,
        int(globalparameter.extract_number * ratio), globalparameter.extract_number,
        globalparameter.extract_number + int((globalparameter.total_number - globalparameter.extract_number) * ratio))
    major_dummy_array = extract_multivalue_feature.extractmajor(
        folderpath + '/' + 'output_pos_for_dummy.csv',
        folderpath + '/' + 'output_neg_for_dummy.csv', 0,
        int(globalparameter.extract_number * ratio), globalparameter.extract_number,
        globalparameter.extract_number + int((globalparameter.total_number - globalparameter.extract_number) * ratio))
    school_dummy_array = extract_multivalue_feature.extractschool(
        folderpath + '/' + 'output_pos_for_dummy.csv',
        folderpath + '/' + 'output_neg_for_dummy.csv', 0,
        int(globalparameter.extract_number * ratio), globalparameter.extract_number,
        globalparameter.extract_number + int((globalparameter.total_number - globalparameter.extract_number) * ratio))

    workcompany_dummy_array1 = extract_multivalue_feature.extractworkcompany(
        folderpath + '/' + 'output_pos_for_dummy.csv',
        folderpath + '/' + 'output_neg_for_dummy.csv', 0,
        int(globalparameter.extract_number * ratio), globalparameter.extract_number,
        globalparameter.extract_number + int((globalparameter.total_number - globalparameter.extract_number) * ratio),
        10)
    workcompany_dummy_array2 = extract_multivalue_feature.extractworkcompany(
        folderpath + '/' + 'output_pos_for_dummy.csv',
        folderpath + '/' + 'output_neg_for_dummy.csv', 0,
        int(globalparameter.extract_number * ratio), globalparameter.extract_number,
        globalparameter.extract_number + int((globalparameter.total_number - globalparameter.extract_number) * ratio),
        16)
    workcompany_dummy_array3 = extract_multivalue_feature.extractworkcompany(
        folderpath + '/' + 'output_pos_for_dummy.csv',
        folderpath + '/' + 'output_neg_for_dummy.csv', 0,
        int(globalparameter.extract_number * ratio), globalparameter.extract_number,
        globalparameter.extract_number + int((globalparameter.total_number - globalparameter.extract_number) * ratio),
        22)
    workcompany_dummy_array4 = extract_multivalue_feature.extractworkcompany(
        folderpath + '/' + 'output_pos_for_dummy.csv',
        folderpath + '/' + 'output_neg_for_dummy.csv', 0,
        int(globalparameter.extract_number * ratio), globalparameter.extract_number,
        globalparameter.extract_number + int((globalparameter.total_number - globalparameter.extract_number) * ratio),
        28)
    workcompany_dummy_array5 = extract_multivalue_feature.extractworkcompany(
        folderpath + '/' + 'output_pos_for_dummy.csv',
        folderpath + '/' + 'output_neg_for_dummy.csv', 0,
        int(globalparameter.extract_number * ratio), globalparameter.extract_number,
        globalparameter.extract_number + int((globalparameter.total_number - globalparameter.extract_number) * ratio),
        34)
    workcompany_dummy_array6 = extract_multivalue_feature.extractworkcompany(
        folderpath + '/' + 'output_pos_for_dummy.csv',
        folderpath + '/' + 'output_neg_for_dummy.csv', 0,
        int(globalparameter.extract_number * ratio), globalparameter.extract_number,
        globalparameter.extract_number + int((globalparameter.total_number - globalparameter.extract_number) * ratio),
        40)

    var1 = int(globalparameter.extract_number * ratio)
    var2 = globalparameter.extract_number
    var3 = globalparameter.extract_number + int((globalparameter.total_number - globalparameter.extract_number) * ratio)
    xtrain = len(X_train)
    len_skill_dummy = len(skill_dummy_array)
    len_major_dummy = len(major_dummy_array)
    len_school_dummy = len(school_dummy_array)

    # Reset the index to make sure the sequence of concat data is right
    X_train.index = range(int(globalparameter.total_number * ratio))
    skill_dummy_array.index = range(int(globalparameter.total_number * ratio))
    major_dummy_array.index = range(int(globalparameter.total_number * ratio))
    school_dummy_array.index = range(int(globalparameter.total_number * ratio))
    workcompany_dummy_array1.index = range(int(globalparameter.total_number * ratio))
    workcompany_dummy_array2.index = range(int(globalparameter.total_number * ratio))
    workcompany_dummy_array3.index = range(int(globalparameter.total_number * ratio))
    workcompany_dummy_array4.index = range(int(globalparameter.total_number * ratio))
    workcompany_dummy_array5.index = range(int(globalparameter.total_number * ratio))
    workcompany_dummy_array6.index = range(int(globalparameter.total_number * ratio))

    # new_X_train = X_train
    # new_X_train = pd.concat([X_train, major_dummy_array, school_dummy_array], axis=1, join_axes=[X_train.index])
    # new_X_train = pd.concat([X_train, workcompany_dummy_array1, workcompany_dummy_array2, workcompany_dummy_array3,
    #                          workcompany_dummy_array4, workcompany_dummy_array5, workcompany_dummy_array6], axis=1,
    #                         join_axes=[X_train.index])
    new_X_train = skill_dummy_array

    shape1 = (skill_dummy_array.shape)
    shape2 = new_X_train.shape
    return new_X_train


def bag_of_words_generate_X_test(folderpath, jobtitle, X, ratio):
    # user_profile = pd.DataFrame(pd.read_csv(folderpath + '/test1.csv'))

    # X = user_profile[['normalized_highest_degree', 'normalized_work_year_past1', 'normalized_work_year_past2',
    #                   'normalized_work_year_past3', 'normalized_work_year_past4', 'normalized_work_year_past5',
    #                   'normalized_work_year_past6']]

    # X = X['normalized_highest_degree']

    X = X[['normalized_work_year_past1', 'normalized_work_year_past2',
           'normalized_work_year_past3', 'normalized_work_year_past4', 'normalized_work_year_past5',
           'normalized_work_year_past6']]

    X_test = pd.concat([X.iloc[int(globalparameter.extract_number * ratio):globalparameter.extract_number], X.iloc[int(
        globalparameter.extract_number + (
                globalparameter.total_number - globalparameter.extract_number) * ratio):globalparameter.total_number]])
    skill_dummy_array = extract_multivalue_feature.extractskill(
        folderpath + '/' + 'output_pos_for_dummy.csv',
        folderpath + '/' + 'output_neg_for_dummy.csv',
        int(globalparameter.extract_number * ratio),
        globalparameter.extract_number,
        globalparameter.extract_number + int((globalparameter.total_number - globalparameter.extract_number) * ratio),
        globalparameter.total_number)
    major_dummy_array = extract_multivalue_feature.extractmajor(
        folderpath + '/' + 'output_pos_for_dummy.csv',
        folderpath + '/' + 'output_neg_for_dummy.csv',
        int(globalparameter.extract_number * ratio),
        globalparameter.extract_number,
        globalparameter.extract_number + int((globalparameter.total_number - globalparameter.extract_number) * ratio),
        globalparameter.total_number)
    school_dummy_array = extract_multivalue_feature.extractschool(
        folderpath + '/' + 'output_pos_for_dummy.csv',
        folderpath + '/' + 'output_neg_for_dummy.csv',
        int(globalparameter.extract_number * ratio),
        globalparameter.extract_number,
        globalparameter.extract_number + int((globalparameter.total_number - globalparameter.extract_number) * ratio),
        globalparameter.total_number)

    workcompany_dummy_array1 = extract_multivalue_feature.extractworkcompany(
        folderpath + '/' + 'output_pos_for_dummy.csv',
        folderpath + '/' + 'output_neg_for_dummy.csv',
        int(globalparameter.extract_number * ratio),
        globalparameter.extract_number,
        globalparameter.extract_number + int((globalparameter.total_number - globalparameter.extract_number) * ratio),
        globalparameter.total_number, 10)
    workcompany_dummy_array2 = extract_multivalue_feature.extractworkcompany(
        folderpath + '/' + 'output_pos_for_dummy.csv',
        folderpath + '/' + 'output_neg_for_dummy.csv',
        int(globalparameter.extract_number * ratio),
        globalparameter.extract_number,
        globalparameter.extract_number + int((globalparameter.total_number - globalparameter.extract_number) * ratio),
        globalparameter.total_number, 16)
    workcompany_dummy_array3 = extract_multivalue_feature.extractworkcompany(
        folderpath + '/' + 'output_pos_for_dummy.csv',
        folderpath + '/' + 'output_neg_for_dummy.csv',
        int(globalparameter.extract_number * ratio),
        globalparameter.extract_number,
        globalparameter.extract_number + int((globalparameter.total_number - globalparameter.extract_number) * ratio),
        globalparameter.total_number, 22)
    workcompany_dummy_array4 = extract_multivalue_feature.extractworkcompany(
        folderpath + '/' + 'output_pos_for_dummy.csv',
        folderpath + '/' + 'output_neg_for_dummy.csv',
        int(globalparameter.extract_number * ratio),
        globalparameter.extract_number,
        globalparameter.extract_number + int((globalparameter.total_number - globalparameter.extract_number) * ratio),
        globalparameter.total_number, 28)
    workcompany_dummy_array5 = extract_multivalue_feature.extractworkcompany(
        folderpath + '/' + 'output_pos_for_dummy.csv',
        folderpath + '/' + 'output_neg_for_dummy.csv',
        int(globalparameter.extract_number * ratio),
        globalparameter.extract_number,
        globalparameter.extract_number + int((globalparameter.total_number - globalparameter.extract_number) * ratio),
        globalparameter.total_number, 34)
    workcompany_dummy_array6 = extract_multivalue_feature.extractworkcompany(
        folderpath + '/' + 'output_pos_for_dummy.csv',
        folderpath + '/' + 'output_neg_for_dummy.csv',
        int(globalparameter.extract_number * ratio),
        globalparameter.extract_number,
        globalparameter.extract_number + int((globalparameter.total_number - globalparameter.extract_number) * ratio),
        globalparameter.total_number, 40)

    var1 = int(globalparameter.extract_number * ratio)
    var2 = globalparameter.extract_number
    var3 = globalparameter.extract_number + int((globalparameter.total_number - globalparameter.extract_number) * ratio)
    var4 = globalparameter.total_number
    xtrain = len(X_test)
    len_skill_dummy = len(skill_dummy_array)
    len_major_dummy = len(major_dummy_array)
    len_school_dummy = len(school_dummy_array)

    # Reset the index to make sure the sequence of concat data is right
    X_test.index = range(int(globalparameter.total_number * (1 - ratio)))
    skill_dummy_array.index = range(int(globalparameter.total_number * (1 - ratio)))
    major_dummy_array.index = range(int(globalparameter.total_number * (1 - ratio)))
    school_dummy_array.index = range(int(globalparameter.total_number * (1 - ratio)))
    workcompany_dummy_array1.index = range(int(globalparameter.total_number * (1 - ratio)))
    workcompany_dummy_array2.index = range(int(globalparameter.total_number * (1 - ratio)))
    workcompany_dummy_array3.index = range(int(globalparameter.total_number * (1 - ratio)))
    workcompany_dummy_array4.index = range(int(globalparameter.total_number * (1 - ratio)))
    workcompany_dummy_array5.index = range(int(globalparameter.total_number * (1 - ratio)))
    workcompany_dummy_array6.index = range(int(globalparameter.total_number * (1 - ratio)))

    # new_X_test = X_test
    # new_X_test = pd.concat([X_test, major_dummy_array, school_dummy_array], axis=1, join_axes=[X_test.index])
    # new_X_test = pd.concat(
    #     [X_test, workcompany_dummy_array1, workcompany_dummy_array2, workcompany_dummy_array3, workcompany_dummy_array4,
    #      workcompany_dummy_array5, workcompany_dummy_array6], axis=1, join_axes=[X_test.index])
    new_X_test = skill_dummy_array
    shape1 = (skill_dummy_array.shape)
    shape2 = new_X_test.shape
    return new_X_test



def bag_of_words():

    return