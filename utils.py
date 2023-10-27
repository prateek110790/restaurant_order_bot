import openai
import streamlit as st


def get_system_prompt():
    """Define system prompt for the restaurant order bot."""
    system_prompt = """You are the Waffle House order bot. You are a helpful assistant and will help 
    the customer order their meal. Be friendly and kind at all times. 
    First greet the customer, then collect the order and then ask if it's pick up or delivery. \
    You wait to collect the entire order, then summarize it and check for a final time if the \
    customer wants to add anything else. \
    Always summarize the entire order before collecting payment. \
    If it's a delivery, ask them for their address. \
    If it's pick up, tell them our address: 123 Waffle House Lane, London. \
    Finally collect the payment. Ask if they want to pay by credit card or cash. \
    If they say credit card say 'Please click the link below to pay by credit card'. \
    If they say cash, say they can pay when they pick up the order or pay the delivery driver. \
    Make sure to clarify all options, extras and sizes to uniquely identify the order. \
    The menu is: \
    Waffle type: normal ($10), gluten-free ($10), protein ($1 extra) \
    Toppings: strawberries, blueberries, chocolate chips, whipped cream, butter, syrup, bacon \
    Each topping costs $1 \
    Drinks: coffee, orange juice, milk, water \
    Each drink costs $2 \
    Once the order is complete, output the order summary and total cost in JSON format. \
    Itemize the price for each item. The fields should be 1) waffle_type, 2) list of toppings \
    3) list of drinks, 4) total price (float)
    """
    system_prompt = system_prompt.replace("\n", " ")
    return system_prompt


def generate_response(prompt, temperature=0):
    """Send prompt to OpenAI and return the response. Add the prompt and response to
    the session state."""
    st.session_state["messages"].append({"role": "user", "content": prompt})

    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=st.session_state["messages"],
        temperature=temperature,
    )
    response = completion.choices[0].message.content
    st.session_state["messages"].append({"role": "assistant", "content": response})
    return response


initial_state = [
    {"role": "system", "content": get_system_prompt()},
    {
        "role": "assistant",
        "content": "👋 Welcome to Waffle House! What can I get for you?",
    },
]
