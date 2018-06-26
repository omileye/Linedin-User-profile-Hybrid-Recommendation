import workexperiecetimes, non_calculatedegreeworkyear, calculatedegreeworkyear, datanormalize, generateweightingfile, \
    calculatecosinesimilarity, diagramgenerator, datafilter, calculate_data_job_now, alg_logestic_regression, alg_svm, \
    alg_bayes, alg_decision_tree, alg_ramdom_forest, extract_multivalue_feature, generate_train_test_set, \
    calculate_baseline, bag_of_words
import globalparameter
import time


def contentbased(positivesamplevalue):
    globalparameter.extract_number = positivesamplevalue
    workexperiecetimes.calculate_work_exp_times(globalparameter.path, globalparameter.name_for_search_exp_times,
                                                globalparameter.job_title_name, globalparameter.job_title_data_path,
                                                globalparameter.output_file_header_job_title,
                                                globalparameter.extract_number)
    workexperiecetimes.calculate_work_exp_times(globalparameter.path, globalparameter.name_for_search_exp_times,
                                                globalparameter.job_title_name, globalparameter.non_job_title_data_path,
                                                globalparameter.output_file_header_non_job_title,
                                                (globalparameter.total_number - globalparameter.extract_number))
    calculatedegreeworkyear.calculate_highest_degree(globalparameter.path, globalparameter.job_title_name,
                                                     globalparameter.job_title_data_path,
                                                     (globalparameter.extract_number))
    calculatedegreeworkyear.calculate_work_year(globalparameter.path, globalparameter.job_title_name,
                                                globalparameter.job_title_data_path,
                                                globalparameter.extract_number)
    non_calculatedegreeworkyear.non_calculate_highest_degree(globalparameter.path, globalparameter.job_title_name,
                                                             globalparameter.non_job_title_data_path,
                                                             (globalparameter.extract_number))
    non_calculatedegreeworkyear.non_calculate_work_year(globalparameter.path, globalparameter.job_title_name,
                                                        globalparameter.non_job_title_data_path,
                                                        (globalparameter.extract_number))

    time.sleep(1)
    calculatecosinesimilarity.content_based_doc_generator(globalparameter.extract_number)
    calculatecosinesimilarity.calculatecosinesililarity()
    generateweightingfile.generateweighting()
    datanormalize.normalize_weighting_highest_degree(globalparameter.path + '/test.csv')
    diagramgenerator.calculateprecisionandrecall(globalparameter.extract_number)


def function(index):
    contentbased(index)
    diagramgenerator.generatediagram(globalparameter.cosine_similarity_column_precision,
                                     globalparameter.cosine_similarity_column_recall,
                                     globalparameter.name_for_search_cosine_similarity, index, 1)
    diagramgenerator.generatediagram(globalparameter.work_year_column_precision,
                                     globalparameter.work_year_column_recall,
                                     globalparameter.name_for_search_work_year, index, 2)
    diagramgenerator.generatediagram(globalparameter.highest_degree_column_precision,
                                     globalparameter.highest_degree_column_recall,
                                     globalparameter.name_for_search_highest_degree, index, 3)
    diagramgenerator.generatediagram(globalparameter.exp_time_column_precision,
                                     globalparameter.exp_time_column_recall,
                                     globalparameter.name_for_search_exp_times, index, 4)
    globalparameter.cosine_similarity_column_precision = []
    globalparameter.cosine_similarity_column_recall = []
    globalparameter.work_year_column_precision = []
    globalparameter.work_year_column_recall = []
    globalparameter.highest_degree_column_precision = []
    globalparameter.highest_degree_column_recall = []
    globalparameter.exp_time_column_precision = []
    globalparameter.exp_time_column_recall = []


if __name__ == '__main__':
    # for i in range(6):
    #     datafilter.filter_alluser_with_newest_jobtitle(globalparameter.raw_data_path, globalparameter.folderpath[i],
    #                                                    globalparameter.jobtitle_path_list[i],
    #                                                    globalparameter.jobtitle_list[i])
    # for i in range(6):
    #     calculate_data_job_now.calculate_work_year_except_newest(globalparameter.folderpath[i],
    #                                                              globalparameter.folderpath[
    #                                                                  i] + '/' + globalparameter.jobtitle_path_list[
    #                                                                  i] + globalparameter.output_file_root,
    #                                                              globalparameter.jobtitle_path_list[i],
    #                                                              globalparameter.jobtitle_list[i],
    #                                                              globalparameter.extract_number)
    #     calculate_data_job_now.calculate_work_year_except_newest(globalparameter.folderpath[i],
    #                                                              globalparameter.folderpath[
    #                                                                  i] + '/non_' + globalparameter.jobtitle_path_list[
    #                                                                  i] + globalparameter.output_file_root,
    #                                                              '/non_' + globalparameter.jobtitle_path_list[i],
    #                                                              globalparameter.jobtitle_list[i],
    #                                                              globalparameter.total_number * 2)
    for i in range(6):
        print('generating highest degree of user: '+str(globalparameter.job_title_data_path[i]))
        calculatedegreeworkyear.calculate_highest_degree(globalparameter.folderpath[i],
                                                         globalparameter.jobtitle_list[i],
                                                         globalparameter.folderpath[i] + '/' +
                                                         globalparameter.jobtitle_path_list[
                                                             i] + globalparameter.output_file_root,
                                                         globalparameter.jobtitle_path_list[i],
                                                         globalparameter.extract_number)
        print('generating non relevant highest degree of user: '+str(globalparameter.job_title_data_path[i]))
        non_calculatedegreeworkyear.non_calculate_highest_degree(globalparameter.folderpath[i],
                                                                 globalparameter.jobtitle_list[i],
                                                                 globalparameter.folderpath[i] + '/' +
                                                                 'non_' + globalparameter.jobtitle_path_list[
                                                                     i] + globalparameter.output_file_root,
                                                                 'non_' + globalparameter.jobtitle_path_list[i],
                                                                 globalparameter.total_number * 2)
        print('calculate work experience times: '+str(globalparameter.job_title_data_path[i]))
        workexperiecetimes.calculate_work_exp_times(globalparameter.folderpath[i],
                                                    globalparameter.name_for_search_exp_times,
                                                    globalparameter.jobtitle_list[i], globalparameter.folderpath[
                                                        i] + '/' + globalparameter.jobtitle_path_list[
                                                        i] + globalparameter.output_file_root,
                                                    '/' + globalparameter.jobtitle_path_list[i] + '_',
                                                    globalparameter.extract_number)
        print('calculate work experience times: '+str(globalparameter.job_title_data_path[i]))
        workexperiecetimes.calculate_work_exp_times(globalparameter.folderpath[i],
                                                    globalparameter.name_for_search_exp_times,
                                                    globalparameter.jobtitle_list[i], globalparameter.folderpath[
                                                        i] + '/non_' + globalparameter.jobtitle_path_list[
                                                        i] + globalparameter.output_file_root,
                                                    '/non_' + globalparameter.jobtitle_path_list[i] + '_',
                                                    globalparameter.total_number * 2)
        print('generating weighting file of: '+str(globalparameter.job_title_data_path[i]))
        calculate_data_job_now.generateweighting_expect_newest(globalparameter.extract_number,
                                                               globalparameter.folderpath[i],
                                                               globalparameter.jobtitle_path_list[i])
        print('normalizing weighting of '+str(globalparameter.job_title_data_path[i]))
        datanormalize.normalize_weighting_highest_degree(globalparameter.folderpath[i] + '/test.csv',
                                                         globalparameter.folderpath[i])
    for i in range(6):
        print('------job title is:------')
        print(globalparameter.jobtitle_path_list[i])
        # print('baseline precision value of job title is: ')
        # calculate_baseline.baseline_full_text(globalparameter.jobtitle_list[i])
        # calculate_baseline.baseline_work_exp(globalparameter.jobtitle_list[i])
        alg_logestic_regression.logestic_regression(globalparameter.folderpath[i],
                                                    globalparameter.jobtitle_path_list[i], 0.5)
        # alg_svm.svm_classification(globalparameter.folderpath[i], globalparameter.jobtitle_path_list[i], 0.5)
        # alg_bayes.naive_bayes(globalparameter.folderpath[i], globalparameter.jobtitle_path_list[i], 0.5)
        # alg_decision_tree.decision_tree(globalparameter.folderpath[i], globalparameter.jobtitle_path_list[i], 0.5)
        # alg_ramdom_forest.random_forest(globalparameter.folderpath[i], globalparameter.jobtitle_path_list[i], 0.5)
        print('------------')
    # words_list = bag_of_words.extractall_information(globalparameter.folderpath[0]+'/'+globalparameter.jobtitle_path_list[0]+globalparameter.output_file_root,globalparameter.folderpath[0]+'/non_'+globalparameter.jobtitle_path_list[0]+globalparameter.output_file_root,0,
    #     int(globalparameter.extract_number * 0.5), globalparameter.extract_number,
    #     globalparameter.extract_number + int((globalparameter.total_number - globalparameter.extract_number) * 0.5),globalparameter.extract_column_list)
    print(1)
    # for i in range(1,10,1):
    #     function(i)
    # print(1)
