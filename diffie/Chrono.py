import time

class Chronometre:
    def __init__(self):
        self.start = time.time()
        self.end = None
        self.elapsed = [] #une liste des temps écoulés
    
    def stop(self):
        self.end = time.time()
        self.elapsed.append(self.end - self.start)
        print("Temps écoulé: ", self.end - self.start)
        return self.end - self.start

    def restart(self):
        self.start = time.time()
        self.end = None
        self.elapsed = []
    
    def get_elapsed(self):
        self.elapsed.append(time.time() - self.start)
        return self.elapsed[-1]
    
    def get_elapsed_list(self):
        self.elapsed.append(time.time() - self.start)
        return self.elapsed
    
    def affiche_chrono(self):
        print("Temps écoulé: ", time.time() - self.start)