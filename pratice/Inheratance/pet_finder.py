class animal:

    def __init__(self, lang):
        self.lang =  lang
    
    @staticmethod
    def your_pet():
        print("You got a  is animal")
class pet(animal):

    def __init__(self, lang):
        super().__init__(lang)
    
    if(lang == "bark"):
        
     