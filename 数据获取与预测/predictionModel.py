# predictionModel.py
# 预测模型 最近修改2021-7-23
# 环境依赖：scikit-learn 0.19.2
# 作者：58119303曾晗
# 调整者：58119327罗卓彦
# 加入了2020部分数据，部分参数写得比较死。

import pandas as pd
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
import dataGet_2_0
from sklearn.ensemble import RandomForestRegressor


class PredictionModel:
    def __init__(self, data: pd.DataFrame, category: str):
        """
        初始化，创建SVR模型
        :param data: 初始化数据，DataFrame格式，m行n列，每行是一个学校+专业，每列分别是各年的排名
        :param category: 科类，对不同的科类参数不同
        """
        self.scaler = StandardScaler()
        self.data = data
        # 1:
        if category == "sci":
            self.svr = SVR(C=1.1e3, epsilon=1e-2)  # 这边的超参数等有数据了必须再调整
        elif category == "art":
            self.svr = SVR(C=2e3, epsilon=1e-2)  # 这边的超参数等有数据了必须再调整
        else:
            raise ValueError("文科：'art'，理科：'sci'")
        # 上面这两个参数不许动！
        # 挑了半天才定下这两个参数，调参侠泪目
        # 上面两个参数挑的不错:)
        # 吐了，搞了很久理科然后发现文科不行，调了文科又发现理科不行了
        # 文理的排名区间不大一样，得分开来调
        # 2:
        if category == "sci":
            # 采用polyRegression方法来进行预测
            self.poly = PolynomialFeatures(degree=12)
            # 由于清北人大的存在，需要尽量过拟合的方法来权衡
            self.ridge = Ridge(alpha=1e-3)
            # 由于扩大数据规模所以需要岭回归来进行防止太容易过拟合
        elif category == "art":
            self.poly = PolynomialFeatures(degree=9)
            self.ridge = Ridge(alpha=0.4)
        else:
            raise ValueError("文科：'art'，理科：'sci'")
        # 吐了，新增了2020数据以后poly也给我调了一个上午
        # 3:
        self.treeRegressor = RandomForestRegressor(n_estimators=250)
        # 效果不好，最好的还是多项式回归那个

    def fit_predict_randomForest(self) -> list:
        data = self.data  # 浅复制
        # data一共六列，分别是
        # 学校名，专业名，2017位次，2018位次，2019位次，2020位次
        X_1 = data.iloc[:, 2:4]  # 取2017，2018列为X_1
        X_2 = data.iloc[:, 3:5]  # 取2018，2019列为X_2
        X_test = data.iloc[:, 4:6]  # 取2019，2020列为X_test
        y_1 = data.iloc[:, 4]  # 取2019列为预测变量y_1
        y_2 = data.iloc[:, 5]  # 取2020列为预测变量y_2
        y_1 = y_1.to_frame()
        y_2 = y_2.to_frame()

        # 合并X_1，X_2和y_1，y_2
        X_1.columns = X_2.columns = [0, 1]  # 统一列名，合并不会出错
        y_1.columns = y_2.columns = [0]
        X = pd.concat([X_1, X_2], ignore_index=True)
        y = pd.concat([y_1, y_2], ignore_index=True)

        X_scaled = self.scaler.fit_transform(X)
        X_test_scaled = self.scaler.fit_transform(X_test)
        y_scaled = self.scaler.fit_transform(y)

        self.treeRegressor.fit(X_scaled, y_scaled.squeeze())
        y_pred_scaled = self.treeRegressor.predict(X_test_scaled)

        y_pred = self.scaler.inverse_transform(y_pred_scaled)

        data['2021年（预测，由RandomForest）'] = y_pred.round()  # 取整，加一列，预测结果
        # data是浅复制，自动保存在类属性了

        return y_pred

    def fit_predict_poly(self) -> list:
        """
        用polyRegression拟合数据，并输出下一年的预测
        :param data: DataFrame格式，m行n列，每行是一个学校+专业，每列分别是各年的排名
        :return: 下一年的预测排名列表，按照输入的学校+专业顺序
        """
        data = self.data  # 浅复制
        # data一共六列，分别是
        # 学校名，专业名，2017位次，2018位次，2019位次，2020位次
        X_1 = data.iloc[:, 2:4]  # 取2017，2018列为X_1
        X_2 = data.iloc[:, 3:5]  # 取2018，2019列为X_2
        X_test = data.iloc[:, 4:6]  # 取2019，2020列为X_test
        y_1 = data.iloc[:, 4]  # 取2019列为预测变量y_1
        y_2 = data.iloc[:, 5]  # 取2020列为预测变量y_2
        y_1 = y_1.to_frame()
        y_2 = y_2.to_frame()

        # 合并X_1，X_2和y_1，y_2
        X_1.columns = X_2.columns = [0, 1]  # 统一列名，合并不会出错
        y_1.columns = y_2.columns = [0]
        X = pd.concat([X_1, X_2], ignore_index=True)
        y = pd.concat([y_1, y_2], ignore_index=True)

        X_poly = self.poly.fit_transform(X)
        X_test_poly = self.poly.fit_transform(X_test)

        X_scaled = self.scaler.fit_transform(X_poly)
        X_test_scaled = self.scaler.fit_transform(X_test_poly)
        y_scaled = self.scaler.fit_transform(y)

        ridge = self.ridge.fit(X_scaled, y_scaled.squeeze())
        y_pred_scaled = ridge.predict(X_test_scaled)

        y_pred = self.scaler.inverse_transform(y_pred_scaled)

        data['2021年（预测，由polyRegression）'] = y_pred.round()  # 取整，加一列预测结果
        # data是浅复制，自动保存在类属性了

        return y_pred

    def fit_predict_SVR(self) -> list:
        """
        用SVR拟合数据，并输出下一年的预测
        :param data: DataFrame格式，m行n列，每行是一个学校+专业，每列分别是各年的排名
        :return: 下一年的预测排名列表，按照输入的学校+专业顺序
        """
        data = self.data  # 浅复制
        # data一共六列，分别是
        # 学校名，专业名，2017位次，2018位次，2019位次，2020位次
        X_1 = data.iloc[:, 2:4]  # 取2017，2018列为X_1
        X_2 = data.iloc[:, 3:5]  # 取2018，2019列为X_2
        X_test = data.iloc[:, 4:6]  # 取2019，2020列为X_test
        y_1 = data.iloc[:, 4]  # 取2019列为预测变量y_1
        y_2 = data.iloc[:, 5]  # 取2020列为预测变量y_2
        y_1 = y_1.to_frame()
        y_2 = y_2.to_frame()

        # 合并X_1，X_2和y_1，y_2
        X_1.columns = X_2.columns = [0, 1]  # 统一列名，合并不会出错
        y_1.columns = y_2.columns = [0]
        X = pd.concat([X_1, X_2], ignore_index=True)
        y = pd.concat([y_1, y_2], ignore_index=True)

        X_scaled = self.scaler.fit_transform(X)  # 标准化
        X_test_scaled = self.scaler.fit_transform(X_test)
        y_scaled = self.scaler.fit_transform(y)

        self.svr.fit(X_scaled, y_scaled.squeeze())  # 拟合
        y_pred_scaled = self.svr.predict(X_test_scaled)

        y_pred = self.scaler.inverse_transform(y_pred_scaled)

        data['2021年（预测，由SVR）'] = y_pred.round()  # 取整，加一列，预测结果
        # data是浅复制，自动保存在类属性了

        return y_pred

    def saveToCSV(self, fileName):
        """
        保存为.csv文件
        :param fileName: 文件名
        :return: None
        """
        self.data.to_csv(path_or_buf=fileName, index=False, encoding="utf-8-sig",
                         header=["school", "major", "2017", "2018", "2019", "2020",
                                 "rankEstimatedByPoly", "rankEstimatedBySVR", "avg", "cov"])

    def getAverage(self):
        X = self.data.loc[:, "2017位次":"2020位次"]
        self.data["平均值"] = X.mean(axis=1)

    def getStdDev(self):
        X = self.data.loc[:, "2017位次":"2020位次"]
        self.data["标准差"] = X.std(axis=1)


if __name__ == "__main__":
    sciData = dataGet_2_0.trainData(aim_category="理科")[1]  # 理科排名
    artData = dataGet_2_0.trainData(aim_category="文科")[1]  # 文科排名
    sciModel = PredictionModel(sciData, "sci")
    sciPredPoly = sciModel.fit_predict_poly()
    sciPredSVR = sciModel.fit_predict_SVR()

    sciModel.getAverage()
    sciModel.getStdDev()
    sciModel.saveToCSV("江苏省理科预测数据.csv")

    artModel = PredictionModel(artData, "art")
    artPredPoly = artModel.fit_predict_poly()
    artPredSVR = artModel.fit_predict_SVR()

    artModel.getAverage()
    artModel.getStdDev()
    artModel.saveToCSV("江苏省文科预测数据.csv")
