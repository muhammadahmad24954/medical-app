import os
class MedicationPrescriptionApp:
    def __init__(self):
        self.data = self.load_data()

    def load_data(self):
        return [
            {"name": "Drug A", "salt": "Sodium Chloride", "price": 100},
            {"name": "Drug B", "salt": "Potassium Chloride", "price": 150.5},
            {"name": "Drug C", "salt": "Magnesium Sulfate", "price": 120.75},
            {"name": "Drug D", "salt": "Sodium Chloride", "price": 1000},
            {"name": "Drug E", "salt": "Potassium Chloride", "price": 1500.5},
            {"name": "Drug F", "salt": "Magnesium Sulfate", "price": 1200.75},
        ]

    def search_medication(self, medication_name):
        input_med = next((med for med in self.data if med['name'].lower() == medication_name.lower()), None)
        
        if not input_med:
            return "Medication not found in the database."
        
        input_salt = input_med['salt']
        input_price = input_med['price']
        
        similar_meds = [med for med in self.data if med['salt'] == input_salt and med['name'] != input_med['name']]
        
        result = f"Name: {input_med['name']}\nSalt Type: {input_salt}\nPrice: ${input_price:.2f}\n\nSimilar Medications:\n"
        for med in similar_meds:
            result += f"{med['name']} - {med['salt']} - ${med['price']:.2f}\n"
        
        return result

def main():
    app = MedicationPrescriptionApp()
    while True:
        medication_name = input("Enter medication name (or 'quit' to exit): ").strip()
        if medication_name.lower() == 'quit':
            break
        result = app.search_medication(medication_name)
        print("\n" + result + "\n")

if __name__ == "__main__":
    main()
