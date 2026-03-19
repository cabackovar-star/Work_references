class Results:
    def __init__(self, victories, draws, losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses


class Football(Results):
    def number_of_wins(self):
        return f"футбольных побед: {self.victories}"
    
    def number_of_draws(self):
        return f"футбольных ничьих: {self.draws}"
    
    def number_of_losses(self):
        return f"футбольных поражений: {self.losses}"
    
    def total_points(self):
        points = 3 * self.victories + self.draws
        return f"общее количество очков: {points}"


class Hockey(Results):
    def number_of_wins(self):
        return f"хоккейных побед: {self.victories}"
    
    def number_of_draws(self):
        return f"хоккейных ничьих: {self.draws}"
    
    def number_of_losses(self):
        return f"хоккейных поражений: {self.losses}"
    
    def total_points(self):
        points = 2 * self.victories + self.draws
        return f"общее количество очков: {points}"

football_team = Football(2, 2, 2)
hockey_team = Hockey(2, 2, 2)

for team in [football_team, hockey_team]:
    print(team.number_of_wins())
    print(team.number_of_draws())
    print(team.number_of_losses())
    print(team.total_points())
    print()  # Пустая строка для разделения