def sample_responses(input_text):
    user_message = str(input_text).lower()
    text = input_text
    if user_message in ("help", "/help"):
        return "Hi, just send a message and the bot will reply with the one that's going to bypass the algorithms \nFor more info contact me on through my website \nhttps://ahmad-fawzy.com/"
    if user_message in ("about", "/about"):
        return "This bot was fully programmed and made by Ahmad Fawzy \nWebsite https://ahmad-fawzy.com/"
    if user_message in ("supported_languages", "/supported_languages"):
      return 'This bot helps you to get around Instagram and Facebook comment filters, allowing you to simply hate and insult people who deserve it as much as you want without the fear of being restricted or banned. The bot currently supports "English, Arabic, Persian, French, German, Spanish, Portuguese, Irish, and Dutch"'
    for i in range(len(text)):
        text = text.replace('a', '开')
        text = text.replace('b', 'ხ')
        text = text.replace('c', '¢')
        text = text.replace('d', 'ð')
        text = text.replace('e', 'ε')
        text = text.replace('f', 'ƒ')
        text = text.replace('g', 'ɠ')
        text = text.replace('h', 'ん')
        text = text.replace('i', 'Ꭵ')
        text = text.replace('j', 'よ')
        text = text.replace('k', 'ƙ')
        text = text.replace('l', 'ℓ')
        text = text.replace('m', 'ɱ')
        text = text.replace('n', 'ɳ')
        text = text.replace('o', 'ტ')
        text = text.replace('p', 'Þ')
        text = text.replace('q', 'զ')
        text = text.replace('r', 'ɾ')
        text = text.replace('s', 'ʂ')
        text = text.replace('t', '七')
        text = text.replace('u', 'µ')
        text = text.replace('v', 'ט')
        text = text.replace('w', 'щ')
        text = text.replace('x', 'א')
        text = text.replace('y', 'ყ')
        text = text.replace('z', 'ƶ')
    return text
