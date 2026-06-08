print("=" * 65)
print("🤖 AI CAREER NAVIGATOR PRO")
print("🚀 Smart Career Recommendation System")
print("=" * 65)

# User Details
name = input("\n👤 Enter Your Name: ")
age = input("🎂 Enter Your Age: ")
college = input("🏫 Enter Your College Name: ")

print("\nRate Your Skills (1-10)")
print("-" * 30)

python_skill = int(input("🐍 Python: "))
ml_skill = int(input("🤖 Machine Learning: "))
sql_skill = int(input("🗄️ SQL: "))
java_skill = int(input("☕ Java: "))
web_skill = int(input("🌐 Web Development: "))

# Analysis
total_score = python_skill + ml_skill + sql_skill + java_skill + web_skill
profile_strength = (total_score / 50) * 100

# Strong & Weak Skills
skills = {
    "Python": python_skill,
    "Machine Learning": ml_skill,
    "SQL": sql_skill,
    "Java": java_skill,
    "Web Development": web_skill
}

strong_skills = []
weak_skills = []

for skill, score in skills.items():
    if score >= 7:
        strong_skills.append(skill)
    elif score <= 4:
        weak_skills.append(skill)

# Career Recommendation
if python_skill >= 7 and ml_skill >= 7:
    career = "AI Engineer"
    roadmap = [
        "Deep Learning",
        "Generative AI",
        "MLOps",
        "LangChain",
        "Vector Databases"
    ]
    salary = "₹8 - ₹15 LPA"
    confidence = 95

elif python_skill >= 7 and sql_skill >= 6:
    career = "Data Scientist"
    roadmap = [
        "Statistics",
        "Power BI",
        "Data Analytics",
        "Machine Learning",
        "Data Engineering"
    ]
    salary = "₹6 - ₹12 LPA"
    confidence = 90

elif java_skill >= 7:
    career = "Backend Developer"
    roadmap = [
        "Spring Boot",
        "REST APIs",
        "Microservices",
        "Databases",
        "System Design"
    ]
    salary = "₹5 - ₹10 LPA"
    confidence = 88

elif web_skill >= 7:
    career = "Frontend Developer"
    roadmap = [
        "JavaScript",
        "React",
        "Next.js",
        "UI/UX Design",
        "TypeScript"
    ]
    salary = "₹4 - ₹9 LPA"
    confidence = 85

else:
    career = "Software Developer"
    roadmap = [
        "DSA",
        "Problem Solving",
        "Projects",
        "Git & GitHub",
        "System Design Basics"
    ]
    salary = "₹4 - ₹8 LPA"
    confidence = 75

# Report
print("\n" + "=" * 65)
print("📊 AI CAREER ANALYSIS REPORT")
print("=" * 65)

print(f"\n👤 Name: {name}")
print(f"🎂 Age: {age}")
print(f"🏫 College: {college}")

print(f"\n📈 Profile Strength: {profile_strength:.1f}%")

print("\n💪 Strong Skills:")
if strong_skills:
    for skill in strong_skills:
        print("   ✓", skill)
else:
    print("   None")

print("\n📉 Skills To Improve:")
if weak_skills:
    for skill in weak_skills:
        print("   ✗", skill)
else:
    print("   Great job! No major weak skills.")

print("\n🎯 Recommended Career")
print("➡️", career)

print("\n📚 Learning Roadmap")
for step in roadmap:
    print("   •", step)

print("\n💰 Expected Salary")
print("➡️", salary)

print("\n📊 Recommendation Confidence")
print(f"➡️ {confidence}%")

print("\n🔥 Career Success Message")
print(f"{name}, your profile strongly aligns with {career}.")
print("Keep building projects and upgrading your skills.")
print("Your future looks promising! 🚀")

print("\n" + "=" * 65)
print("🙏 Thank You For Using AI Career Navigator Pro")
print("=" * 65)