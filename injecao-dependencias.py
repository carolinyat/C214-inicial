# Interface para comportamento de cachorro
class DogBehavior:
    def execute(self):
        pass

# Implementação de comportamento para cachorros que latem
class BarkingBehavior(DogBehavior):
    def execute(self):
        return "O cachorro está latindo!"

# Implementação de comportamento para cachorros que correm
class RunningBehavior(DogBehavior):
    def execute(self):
        return "O cachorro está correndo!"

# Serviço que utiliza o comportamento do cachorro
class DogService:
    def __init__(self, behavior: DogBehavior):
        self.behavior = behavior
    
    def perform_behavior(self):
        action = self.behavior.execute()
        print(action)

# Injeção de dependência manual
barking_behavior = BarkingBehavior()
running_behavior = RunningBehavior()

# Usando o serviço com o comportamento de latir
dog_service = DogService(barking_behavior)
dog_service.perform_behavior()  # Saída: O cachorro está latindo!

# Usando o serviço com o comportamento de correr
dog_service = DogService(running_behavior)
dog_service.perform_behavior()  # Saída: O cachorro está correndo!
