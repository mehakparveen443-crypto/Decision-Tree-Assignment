def career_decision_tree():
    print("=" * 40)
    print("🎓 Career Decision Helper")
    print("=" * 40)
    print("Start\n")

    # Q1
    q1 = input("Q1: Are you interested in Data & Numbers? (yes/no): ").strip().lower()

    if q1 == "yes":
        print("\n➡ You chose: Data & Numbers")

        # Q2
        q2 = input("Q2: Do you know Excel / SQL / Python basics? (yes/no): ").strip().lower()

        if q2 == "yes":
            print("\n✅ Action: Prepare for Data Analyst role 📊")
        elif q2 == "no":
            print("\n📚 Action: Learn Data Analytics skills first")
        else:
            print("\n❌ Invalid input at Q2")

    elif q1 == "no":
        print("\n➡ You chose: Not Data field")

        # Q3
        q3 = input("Q3: Are you interested in designing & websites? (yes/no): ").strip().lower()

        if q3 == "yes":
            print("\n💻 Action: Go for Web Development")
        elif q3 == "no":
            print("\n🎓 Action: Consider Higher Studies / Other fields")
        else:
            print("\n❌ Invalid input at Q3")

    else:
        print("\n❌ Invalid input at Q1")

    print("\nEnd")
    print("=" * 40)


# Run program
career_decision_tree()