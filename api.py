import paralleldots
# Setting your API key
paralleldots.set_api_key( "7y5v28wP642qwqjVYzkY71agXRWPs3JpBwhir3DGBBI" )

def ner(text):
    ner = paralleldots.ner(text)
    return ner