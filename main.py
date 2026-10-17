from groq import generate_response

def prompt_engineering_activity():
    print("Welcome to thr AI Prompt Engineering Tutorial!")

    vague =input("Enter a vague prompt: ")
    print("\nAI's response to vague prompt:")
    print(generate_response(vague))

    specific = input("\nNow, make it more specific: ")
    print(generate_response(specific))

    context=input("\nNow, add context to your specific prompt: ")
    print("\nAI's response to contextual prompt:")
    print(generate_response(context))

    print("\n----REflection----")
    print("1. How did the AI's resonse change when the prompt was made more specific?")
    print("2. How did the AI's response improve with the added context?")
    print("3. Which prompt produce the most elevent and tailoed response? Why?")

if __name__ =="__main__":
    prompt_engineering_activity()