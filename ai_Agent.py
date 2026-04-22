def ai_career_agent():
    print("🤖 Hello! I am your Career AI Assistant")
    print("I will guide you based on your interests.\n")

    while True:
        q1 = input("Q1: Interested in Data & Numbers? (yes/no): ").strip().lower()

        if q1 == "yes":
            q2 = input("Q2: Do you know Excel/SQL/Python? (yes/no): ").strip().lower()

            if q2 == "yes":
                print("👉 You should prepare for Data Analyst role 📊")
            elif q2 == "no":
                print("👉 First learn Data Analytics skills 📚")
            else:
                print("❌ Invalid input")

        elif q1 == "no":
            q3 = input("Q3: Interested in Designing/Websites? (yes/no): ").strip().lower()

            if q3 == "yes":
                print("👉 You can go for Web Development 💻")
            elif q3 == "no":
                print("👉 Consider other fields or higher studies 🎓")
            else:
                print("❌ Invalid input")

        else:
            print("❌ Invalid input")

        again = input("\nDo you want to try again? (yes/no): ").strip().lower()
        if again != "yes":
            print("👋 Goodbye!")
            break


ai_career_agent()
