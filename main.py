def check_hemoglobin_status(gender, hemoglobin_value):
    if gender.lower() == 'female':
        if 117 <= hemoglobin_value <= 155:
            return "Normal Hemoglobin"
        elif hemoglobin_value < 117:
            return "Low Hemoglobin"
        else:
            return "High Hemoglobin"
    elif gender.lower() == 'male':
        if 134 <= hemoglobin_value <= 167:
            return "Normal Hemoglobin"
        elif hemoglobin_value < 134:
            return "Low Hemoglobin"
        else:
            return "High Hemoglobin"
    else:
        return "Invalid gender input"

def main():
    try:
        gender = input("Enter biological gender (Male/Female): ")
        hemoglobin_value = float(input("Enter hemoglobin value (g/l): "))

        result = check_hemoglobin_status(gender, hemoglobin_value)

        print(f"Hemoglobin Status: {result}")

    except ValueError:
        print("Invalid input. Please enter a valid numerical value for hemoglobin.")

if __name__ == "__main__":
    main()

