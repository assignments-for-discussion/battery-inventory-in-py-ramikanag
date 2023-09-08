def convert_present_capacity_to_soh(present_capacity, rated_capacity):
    soh_percentage = (present_capacity / rated_capacity) * 100
    return soh_percentage

def classify_battery(soh_percentage):
    if soh_percentage > 80:
        return "Healthy"
    elif 65 <= soh_percentage <= 80:
        return "Exchange"
    else:
        return "Failed"

def classify_and_count_batteries(present_capacities):
    counts = {
        "Healthy": 0,
        "Exchange": 0,
        "Failed": 0
    }
    classified_ranges = []

    rated_capacity = 120 
    
    for capacity in present_capacities:
        soh_percentage = convert_present_capacity_to_soh(capacity, rated_capacity)
        classification = classify_battery(soh_percentage)
        classified_ranges.append((capacity, classification))
        counts[classification] += 1

        print(f"Present Capacity: {capacity} Ah")
        print(f"SoH Percentage: {soh_percentage:.2f}%")
        print(f"Classification: {classification}\n")

    return classified_ranges, counts
    
def test_bucketing_by_health():
    print("Counting batteries by SoH...\n")
    present_capacities = [120, 0, 115, 118, 80, 95, 91, 77]
    classified_ranges, counts = classify_and_count_batteries(present_capacities)
    print("Counts:\n")
    for category, count in counts.items():
        print(f"{category}: {count}")
    print("\nDone counting :)")

if __name__ == '__main__':
    test_bucketing_by_health()
