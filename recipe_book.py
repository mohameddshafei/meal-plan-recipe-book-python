class Recipe:
  def __init__(self, name, ingredients, prep_time, calories):
    self.name = name
    self.ingredients = ingredients.split(',')
    self.time = prep_time
    self.calories = calories
# function zyada
def getIngredients(line):
  start = 0
  end = 0
  for i in range(len(line)):
    if line[i]=='[':
      start = i
    if line[i] == ']':
      end = i
  return line[start+1:end]


class MealPlan:
  def __init__(self, Plan_name, PlanID):
    self.Plan_name = Plan_name
    self.PlanID = PlanID
    self.Recipe_List = []

  def add_Recipe(self, recipe):
    self.Recipe_List.append(recipe)

  def save_mealplan_To_file(self, filename):
    Myfile = open(filename, "w")
    for i in self.Recipe_List:
      Myfile.write(i.name + " " + str(i.ingredients) + " " +str(i.time) + " " + str(i.calories) + "\n")
    Myfile.close()

  def load_MealPlan_from_file(self, filename):
    file2 = open(filename, "r")
    lines = file2.readlines()
    for line in lines:
      recipe_data = line.split(" ")
      print("MealPlan info: ")
      print("the name of the recipe is: ", recipe_data[0])
      print("the ingredients are: ", getIngredients(line))
      print("the time of preparation is:", recipe_data[-2])
      print("the amount of calories is:", recipe_data[-1])
    file2.close()


class RecipeBook:
  def __init__(self):
    self.mealplans = []

  def add_mealplan(self, mealplan):
    self.mealplans.append(mealplan)

  def display_mealplans(self):
    for meal in self.mealplans:
      print("Meal plan name: ", meal.Plan_name)
      print("Meal plan ID: ", meal.PlanID)

  def search_mealplan(self, name):
    for meal in self.mealplans:
      if meal.Plan_name.lower() == name.lower():
        return meal
    return None


# Tesing
recipes = []
for i in range(3):
  print('Enter the data of the recipe number', i + 1)
  name = input("Enter the name of the recipe: ")
  ingredients = input("Enter the ingredients in a list:")
  prep_time = int(input("Enter the preparation time: "))
  calories = int(input('Enter the calories in the recipe:'))
  recipe = Recipe(name, ingredients, prep_time, calories)
  recipes.append(recipe)

mealplan1 = MealPlan("Meal plan 1", 1)
mealplan1.add_Recipe(recipes[0])
mealplan1.add_Recipe(recipes[1])
mealplan2 = MealPlan("Meal plan 2", 2)
mealplan2.add_Recipe(recipes[2])

mealplan1.save_mealplan_To_file("yourname_id.txt")
mealplan1.load_MealPlan_from_file("yourname_id.txt")

book = RecipeBook()
book.add_mealplan(mealplan1)
book.add_mealplan(mealplan2)

book.display_mealplans()

mealplan_search = input("Enter the name of the meal plan to search for: ")
final = book.search_mealplan(mealplan_search)
if final:
  print(mealplan_search, "found!")
else:
  print(mealplan_search, "not found.")
