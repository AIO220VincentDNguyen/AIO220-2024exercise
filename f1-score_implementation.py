#Excercise 1: Viết function thực hiện đánh giá classification model bằng F1-Score.
def evaluate_classification_model(tp, fp, fn):
    #Kiểm tra kiểu dữ liệu của tp, fp, fn
    if type(tp) is not int:
        print('tp must be int')
        return
    if type(fp) is not int:
        print('fp must be int')
        return
    if type(fn) is not int:
        print('fn must be int')
        return
    #Kiểm tra  giá trị của tp, fp, fn > 0
    if tp <= 0 or fp <= 0 or fn <= 0:
        print('tp and fb and fn must be greater than zero')
        return
    #Tính precision, recall và F1-score
    precision = tp/(tp + fp)
    recall = tp/(tp+fn)
    f1_score = (2*precision*recall)/(precision + recall)
    #in ra precision, recall và F1-score
    print('precision: ', precision)
    print('recall: ', recall)
    print('f1_score: ', f1_score)

    return f1_score

evaluate_classification_model(2, 3, 4)
evaluate_classification_model('a', 3, 4)
evaluate_classification_model(2, 'a', 4)
evaluate_classification_model(2, 3, 'a')
evaluate_classification_model(2.1, 3, 0)