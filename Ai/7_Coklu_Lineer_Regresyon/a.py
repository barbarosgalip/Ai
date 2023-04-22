 

df = pd.read_csv('data/Advertising.csv', index_col=0)


X = df[['TV', 'radio', 'newspaper']]
y= df['sales']

lr=LinearRegression()
y=y.values.reshape(-1,1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=100)
lr.fit(X_train, y_train)

y_pred=lr.predict(X_test)

indexler = range(1,61)

# Gerçek Data -> Grand Truth
fig, ax = plt.subplots(figsize=(12,8))
ax.plot(indexler, y_test, label='Grand Truth', color='red', linewidth=2)

# Tahmin -> Prediction
ax.plot(indexler, y_pred, label='Prediction', color='green', linewidth=2)

"""plt.title('GERÇEK - PREDICTION')
plt.xlabel('Data Index')
plt.ylabel('Sales')
plt.legend(loc='upper left')
plt.show()"""

x_train_ols=sm.add_constant(X_train)

sm_model=sm.OLS(y_train,x_train_ols)
sonuc=sm_model.fit()

print(sonuc.summary())