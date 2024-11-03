import os

class MedicationPrescriptionApp:
    def __init__(self):
        self.data = []
        
    def load_data(self, file_path):
        self.data = []
        try:
            with open(file_path, 'r') as file:
                # Skip header row
                next(file)
                for line in file:
                    name, salt, price = line.strip().split(',')
                    self.data.append({
                        "name": name,
                        "salt": salt,
                        "price": float(price)
                    })
            return True
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found!")
            return False
        except Exception as e:
            print(f"Error reading file: {e}")
            return False

    def search_medication(self, medication_name):
        input_med = next((med for med in self.data if med['name'].lower() == medication_name.lower()), None)
        
        if not input_med:
            return "Medication not found in the database."
        
        input_salt = input_med['salt']
        input_price = input_med['price']
        
        similar_meds = [med for med in self.data if med['salt'] == input_salt and med['name'] != input_med['name']]
        
        result = f"\nMedication Details:\n"
        result += f"Name: {input_med['name']}\n"
        result += f"Salt Type: {input_salt}\n"
        result += f"Price: ${input_price:.2f}\n"
        
        if similar_meds:
            result += f"\nSimilar Medications with same salt ({input_salt}):\n"
            for med in similar_meds:
                result += f"- {med['name']} (${med['price']:.2f})\n"
        else:
            result += "\nNo similar medications found with the same salt type."
        
        return result

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_welcome():
    clear_screen()
    print("=" * 50)
    print("Welcome to the Medication Prescription System")
    print("=" * 50)
    print("\nThis application allows you to:")
    print("1. Load medication data from a CSV file")
    print("2. Search for medications")
    print("3. View similar medications with the same salt type")
    print("\nPress Enter to continue...")
    input()

def main():
    app = MedicationPrescriptionApp()
    
    display_welcome()
    
    while True:
        clear_screen()
        print("\n=== Medication Search System ===")
        file_path = input("Enter the path to your medication data file (CSV format) or 'quit' to exit: ").strip()
        
        if file_path.lower() == 'quit':
            print("Thank you for using the Medication Search System!")
            break
            
        if app.load_data(file_path):
            print(f"Successfully loaded medication data from {file_path}")
            
            while True:
                medication_name = input("\nEnter medication name (or 'back' to change file, 'quit' to exit): ").strip()
                
                if medication_name.lower() == 'quit':
                    print("Thank you for using the Medication Search System!")
                    return
                elif medication_name.lower() == 'back':
                    break
                    
                result = app.search_medication(medication_name)
                print(result)
                input("\nPress Enter to continue...")
        else:
            print("Please try again with a valid file path.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
