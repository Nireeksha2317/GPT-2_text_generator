from transformers import GPT2Tokenizer, GPT2LMHeadModel

def generate_text(prompt, model_path="./gpt2-finetuned", max_length=80):
    tokenizer = GPT2Tokenizer.from_pretrained(model_path)
    model = GPT2LMHeadModel.from_pretrained(model_path)
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    attention_mask = (input_ids != tokenizer.pad_token_id).long()
    output = model.generate(
        input_ids,
        attention_mask=attention_mask,
        max_length=max_length,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        do_sample=True,
        top_k=40,           # Lower for more focused output
        top_p=0.92,         # Lower for more focused output
        temperature=0.7,    # Lower for more deterministic output
        pad_token_id=tokenizer.eos_token_id,
        eos_token_id=tokenizer.eos_token_id
    )
    generated = tokenizer.decode(output[0], skip_special_tokens=True)
    # Remove the prompt from the output for cleaner display
    return generated[len(prompt):].strip()

if __name__ == "__main__":
    prompt = input("Enter a prompt: ").strip()
    print("Generated text:\n" + generate_text(prompt))