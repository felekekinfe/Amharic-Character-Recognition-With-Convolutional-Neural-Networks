from transformers import GPT2Tokenizer,GPT2LMHeadModel
import torch

tokenizer=GPT2Tokenizer.from_pretrained('rasyosef/gpt2-small-amharic')
model=GPT2LMHeadModel.from_pretrained('rasyosef/gpt2-small-amharic')

def correct_with_gpt2(raw_sentence,max_length):
    input_ids=tokenizer.encode(raw_sentence,return_tensor='pt')

    with torch.no_grad():
        outputs=model.generate(
            input_ids,
            max_length-max_length,
            num_beams=5,
            early_stopping=True,
            no_repeat_ngram_size=2
        )

    corrected=tokenizer.decode(outputs[0],skip_special_tokens=True)
    return corrected.strip()
