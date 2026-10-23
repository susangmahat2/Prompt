from groq import generate_response

def run_activity():
    print("ZERO-SHOT, ONE-SHOT & FEW=SHOT LEARNING ACYIVITY")
    category=input("Enter a category (e.g., animal, food, city):").strip()
    item= input(f"Enter a specific{category}to classify: ").strip()

    if not category or not item:
        print("Please fill in both fields to run the activity.")
        return
    zero_shot=f"Is {item} a {category}? Answer yes or no."
    print("\n--- ZERO-SHOT LEARNING---")
    print(f"Response: {generate_response(zero_shot, temperature=0.3, max_tokens=1024)}")

    one_shot=f"""Example:
category:fruit
Item:apple
Answer: Yes, apple is a fruit.

Now you try:
Category:{category}
Item:{item}
Answer:"""
    print("\n---ONE-SHOT LEARNING---")
    print(f"Response: {generate_response(one_shot, temperature=0.3, max_tokens=1024)}")

    few_shot=f"""Example1:
Category:fruit
Item:Apple
ANswer:Yes, apple is a fruit.

now Try:
Category:{category}
Item:{item}
Answer:"""
    print("\n----FEW-SHOT LEARNING---")
    print(f"Response:{generate_response(few_shot, temperature=0.3,max_tokens=1024)}")

    creative_prompt = f"""Write a one sentence story about the given words.
Example1:Word:moon
Story:The moon lit up the night sky as a little astrounaut began an exciting space adventure.
Word:{item}
Story:"""
    print("\n--- Creative FEW-SHOT EXAMPLE---")
    print(f"Response:{generate_response(creative_prompt, temperature=0.7, max_tokens=1024)}")
    print("\n--- REFLECTION QUESTIONS----")
    print("1. How did the response differ between zero-shot, one-shot, and few-shot")
    print("2.WHich approach gave the most helpful response?")

if __name__=="__main__":
    run_activity()