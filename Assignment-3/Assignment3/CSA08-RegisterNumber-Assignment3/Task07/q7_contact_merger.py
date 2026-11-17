"""Q7: Contact merging from first principles using normalised phone-number keys."""
import random, time, csv, re

def normalise_number(number):
    if not number:
        return ""
    digits = "".join(ch for ch in number if ch.isdigit())
    if digits.startswith("91") and len(digits) == 12:
        digits = digits[2:]
    return digits

def normalise_name(name):
    return " ".join((name or "").lower().replace(".", " ").split())

def merge_contacts(contact_lists):
    merged = {}
    for source in contact_lists:
        for contact in source:
            key = normalise_number(contact.get("phone", ""))
            if not key:
                # Contacts without a phone cannot safely be merged by phone.
                key = "NO_PHONE:" + normalise_name(contact.get("name", "")) + ":" + str(len(merged))
            if key not in merged:
                merged[key] = {"name": contact.get("name", "").strip(),
                               "numbers": set(), "emails": set(), "aliases": set()}
            entry = merged[key]
            if contact.get("name"):
                entry["aliases"].add(contact["name"].strip())
                if not entry["name"]:
                    entry["name"] = contact["name"].strip()
            if contact.get("phone"):
                entry["numbers"].add(contact["phone"].strip())
            if contact.get("email"):
                entry["emails"].add(contact["email"].strip().lower())
    return list(merged.values())

def pairwise_merge(contact_lists):
    result = []
    for source in contact_lists:
        for contact in source:
            key = normalise_number(contact.get("phone", ""))
            match = None
            for existing in result:
                existing_keys = {normalise_number(x) for x in existing["numbers"]}
                if key and key in existing_keys:
                    match = existing; break
            if match is None:
                match = {"name": contact.get("name", ""), "numbers": set(), "emails": set(), "aliases": set()}
                result.append(match)
            if contact.get("name"): match["aliases"].add(contact["name"])
            if contact.get("phone"): match["numbers"].add(contact["phone"])
            if contact.get("email"): match["emails"].add(contact["email"].lower())
    return result

def main():
    phone_a = [
        {"name": "Dr. Ravi", "phone": "+91 98400 12345", "email": "ravi@example.com"},
        {"name": "Meena", "phone": "9876543210", "email": "meena@example.com"},
    ]
    phone_b = [
        {"name": "ravi kumar", "phone": "9840012345", "email": "rk@example.com"},
        {"name": "Arun", "phone": "9000011111", "email": ""},
        {"name": "No phone contact", "phone": "", "email": "none@example.com"},
    ]
    sim = [{"name": "Ravi", "phone": "98400-12345", "email": "RAVI@example.com"}]
    merged = merge_contacts([phone_a, phone_b, sim])
    for item in merged:
        print(item["name"], sorted(item["numbers"]), sorted(item["emails"]), sorted(item["aliases"]))

    rows = []
    for n in (1_000, 100_000):
        contacts = [[{"name": f"Person{i}", "phone": f"{9000000000+i:010d}", "email": ""} for i in range(n)]]
        start = time.perf_counter(); merge_contacts(contacts); dict_time = time.perf_counter()-start
        # Pairwise comparison is intentionally limited for the large case to avoid impractical O(n^2) runtime.
        if n == 1_000:
            start = time.perf_counter(); pairwise_merge(contacts); pair_time = time.perf_counter()-start
        else:
            pair_time = None
        print(f"{n} contacts: dictionary={dict_time:.6f}s pairwise={pair_time}")
        rows.append([n, dict_time, pair_time])
    with open("q7_timings.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["contacts", "dictionary_seconds", "pairwise_seconds"]); w.writerows(rows)

if __name__ == "__main__":
    main()
