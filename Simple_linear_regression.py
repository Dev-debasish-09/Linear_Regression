class LinearRrg:
    def _init_(self):
        self.m = None
        self.b = None
        
    def fit(self,X_train,y_train):
        num=0
        denom=0
        for i in range(X_train.shape[0]):
            
            num = num + ((X_train[i] - X_train.mean())*(y_train[i] - y_train.mean()))
            denom = denom + ((X_train[i] - X_train.mean())*(X_train[i] - X_train.mean()))   
        self.m = num/denom
        self.b = y_train.mean() - (self.m*X_train.mean())
        print(self.m)
        print(self.b)
        
    def predict(self,X_test):
        print(X_test)
        return self.m*X_test+self.b

    def mean_abs_error(self,y_test,y_pred):
        e = np.array(y_test)
        f = np.array(y_pred)
        c = 0
        for i in range(len(y_test)):
          c +=  np.abs(e[i] - f[i])
        return c/len(y_test)

  def mean_squared_error(self,y_test,y_pred):
        e = np.array(y_test)
        f = np.array(y_pred)
        c = 0
        for i in range(len(y_test)):
          c +=  np.abs((e[i] - f[i])**2)
        return c/len(y_test)
