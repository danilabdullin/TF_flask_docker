import os
import pickle
import time

from model_util import DeepModel


class ImageClassifier(DeepModel):
    def __init__(self):
        super().__init__()
        self.all_skus = {}
        self.model = DeepModel()
        self.predict_time = 0
        self.time_search = 0
        self.count_frame = 0


    def predict(self, img):
        ''' Predict the class of image
        Args:
            img: relative path to the image
        Returns:
            tuple with picture name, predicted value, similarity rate, total time spent on prediction and
            time spent on on picture to predict the class
        '''
        step_time = 0
        answer = img.split('/')
        self.count_frame += 1
        before_time = time.time()
        img = self.preprocess_image(img)
        target_features = self.extract_feature(img)
        max_distance = 0
        result_dish = 0

        for dish, features_all in self.all_skus.items():
            for features in features_all:
                cur_distance = self.model.cosine_distance(target_features, features)
                cur_distance = cur_distance[0][0]
                if cur_distance > max_distance:
                    max_distance = cur_distance
                    result_dish = dish
        self.predict_time += time.time() - before_time
        step_time += time.time() - before_time
        return f'predicted value:{result_dish}', \
               f'similarity rate: {max_distance}', \
               f'total time spent: {round(self.predict_time, 4)}', \
               f'time spent for picture: {step_time}'


           #f'Pic name: {answer[3]}', \


    def add_img(self, img_path, id_img):
        '''
        Add embeddings of new picture to dictionary all_skus
        :param img_path: relative path to picture
        :param id_img: str, name of class
        :return: embedding of picture
        '''
        img = self.preprocess_image(img_path)
        cur_img = img
        feature = self.extract_feature(cur_img)
        if id_img not in self.all_skus:
            self.all_skus[id_img] = []
        self.all_skus[id_img].append(feature)
        return feature


    def learn(self, folder_path):
        '''
        Goes through the folder and automatically add embeddings and class name to all_skus
        :param folder_path: relative path to folder with pictures
        :return: None
        '''
        for dirpath, dirnames, filen in os.walk(folder_path):
            for _, __, filenames in os.walk(dirpath):
                for filename in filenames:
                    f = os.path.join(_, filename).replace('\\', '//')
                    t = f.split('/')[3]
                    self.add_img(f, t)



    def get_classes(self):
        '''
        :return: available classes to predict
        '''
        return self.all_skus.keys()

    def remove_by_id(self, id_img):
        '''
        Delete class and its embeddings fom all_skus
        :param id_img: str, name of class
        :return: deleted item
        '''
        if id_img in self.all_skus:
            self.all_skus.pop(id_img)

    def remove_all(self):
        '''

        :return: clears all_skus
        '''
        self.all_skus.clear()

    def add_img_from_pickle(self, id_img, pickle_path):
        res = pickle.load(open(pickle_path, 'rb'))
        self.all_skus[id_img] = res

    def get_additional_info(self):
        json_res = {}
        json_res["Extract features, time"] = self.predict_time
        json_res["Find nearest, time"] = self.time_search
        json_res["Count frame"] = self.count_frame

        return json_res


# if __name__ == "__main__":
#     path = './data'
#     classifier = ImageClassifier()
#     classifier.learn(path)
#
#     path_test = './test_imgs'
#     for dirpath, dirnames, filenames in os.walk(path_test):
#         for file in filenames:
#             image_path = os.path.join(dirpath, file).replace('\\', '//')
#
#             print(classifier.predict(image_path))
#
#     print(classifier.get_classes())