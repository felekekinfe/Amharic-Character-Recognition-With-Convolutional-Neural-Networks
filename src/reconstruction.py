

def reconstruct_sentence(components,characters):

    sentence=[]
    last_x=-20

    for i,(x,y,w,h) in enumerate(components):
        if x-last_x>15:
            sentence.append('')
        sentence.append(characters[i])
        last_x=x+w
        return ''.join(sentence)