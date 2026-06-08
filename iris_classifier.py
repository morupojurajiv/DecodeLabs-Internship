from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

print("=" * 60)
print("🌸 AI IRIS FLOWER CLASSIFICATION SYSTEM")
print("🤖 Powered by Machine Learning (KNN)")
print("=" * 60)

# Load Dataset
iris = load_iris()
X = iris.data
y = iris.target

print("\n✅ Dataset Loaded Successfully")
print(f"📊 Total Samples : {len(X)}")
print(f"📌 Total Features : {len(X[0])}")
print(f"🌼 Flower Classes : {len(iris.target_names)}")

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\n⚙️ Training AI Model...")

# Train Model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

print("✅ Model Trained Successfully")

# Accuracy
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("\n" + "=" * 60)
print("📊 MODEL PERFORMANCE REPORT")
print("=" * 60)

print(f"🎯 Accuracy Score : {accuracy * 100:.2f}%")

print("\n🌼 Available Flower Types")
for flower in iris.target_names:
    print("   •", flower.capitalize())

print("\n" + "=" * 60)
print("🔍 FLOWER PREDICTION SECTION")
print("=" * 60)

print("\nEnter Flower Measurements")

sepal_length = float(input("Sepal Length (cm): "))
sepal_width = float(input("Sepal Width (cm): "))
petal_length = float(input("Petal Length (cm): "))
petal_width = float(input("Petal Width (cm): "))

user_data = [[
    sepal_length,
    sepal_width,
    petal_length,
    petal_width
]]

prediction = model.predict(user_data)

flower_name = iris.target_names[prediction[0]]

print("\n" + "=" * 60)
print("🤖 AI PREDICTION RESULT")
print("=" * 60)

print(f"🌸 Predicted Flower : {flower_name.capitalize()}")

print("\n🔥 Project Status : Successful")
print("✅ Model Working Correctly")
print("✅ Prediction Generated")

print("\n🙏 Thank You For Using")
print("🌸 AI Iris Flower Classification System")
print("=" * 60)