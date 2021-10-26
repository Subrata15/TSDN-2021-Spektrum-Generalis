from pandas.core.algorithms import mode
from pycaret.classification import load_model
import pandas as pd

dict_median = {'KELAPA_HARAPAN':159, 'LANCANG':117, 'MARINA':492, 'ANGKE':645, 'PARI':243, 'PRAMUKA_PANGGANG':260,
 'SABIRA':14, 'TIDUNG_PAYUNG':253, 'UNTUNG_JAWA':240}

def predalt(dict_test):
    path_model = "model_pelabuhan/"

    model = load_model(path_model+"tuned_"+dict_test["Pelabuhan"])

    dict_c = {"Positivity_rate_val":dict_test["Positivity_rate_val"], "Retail_recreation":dict_test["Retail_recreation"]}

    df_ = pd.DataFrame(data=dict_c)

    is_normal = model.predict(df_)

    # decision, rule base # WARNING: BE CAREFUL!
    if is_normal[-1]==0 and dict_test["Sosial"]=="Yes":
        med_ = dict_median[dict_test["Pelabuhan"]]
        result = str(med_)+"<=" # decrease
        return result

    elif is_normal[-1]==0 and dict_test["Sosial"]=="No":
        if dict_test["Retail_recreation"][-1] == 1:
            med_ = dict_median[dict_test["Pelabuhan"]]
            result = ">="+str(med_) # normal/increase
            return result
        elif dict_test["Retail_recreation"][-1] == 0:
            med_ = dict_median[dict_test["Pelabuhan"]]
            result = str(med_)+"<=" # decrease
            return result

    #########################################################

    elif is_normal[-1]==1 and dict_test["Sosial"]=="Yes":
        med_ = dict_median[dict_test["Pelabuhan"]]
        result = ">="+str(med_) # normal/increase
        return result

    elif is_normal[-1]==1 and dict_test["Sosial"]=="No":
        if dict_test["Retail_recreation"][-1] == 1:
            med_ = dict_median[dict_test["Pelabuhan"]]
            result = ">="+str(med_) # normal/increase
            return result
        elif dict_test["Retail_recreation"][-1] == 0:
            med_ = dict_median[dict_test["Pelabuhan"]]
            result = str(med_)+"<=" # decrease
            return result
