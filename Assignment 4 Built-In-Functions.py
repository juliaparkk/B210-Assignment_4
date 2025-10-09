def parse_csv_line(line):
    """Return list of fields from a CSV line handling double-quoted fields and commas inside quotes."""
    fields = []
    cur = []
    in_quotes = False
    i = 0
    while i < len(line):
        ch = line[i]
        if ch == '"':
            # doubled quote inside quoted field -> single quote char
            if in_quotes and i + 1 < len(line) and line[i+1] == '"':
                cur.append('"')
                i += 2
                continue
            in_quotes = not in_quotes
            i += 1
            continue
        if ch == ',' and not in_quotes:
            fields.append(''.join(cur))
            cur = []
            i += 1
            continue
        cur.append(ch)
        i += 1
    last = ''.join(cur)
    if last.endswith('\n'):
        last = last[:-1]
    fields.append(last)
    return [f.strip() for f in fields]


def print_songs_in_energy_range(file_path, min_energy, max_energy):
    """
    Read CSV (expects header containing 'track_name' and 'energy') and print track_name
    values with energy in [min_energy, max_energy]. No external libraries used.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            # read header (skip leading blank lines)
            for header_line in f:
                if header_line.strip() != '':
                    break
            header = parse_csv_line(header_line)
            # remove UTF-8 BOM if present in the first header field
            if len(header) > 0:
                header[0] = header[0].lstrip('\ufeff')
            lower = [h.strip().lower() for h in header]
            # Accept 'track_name' as the track column
            if 'track_name' not in lower or 'energy' not in lower:
                print("CSV header must include 'track_name' and 'energy'. Found:", header)
                return
            name_idx = lower.index('track_name')
            energy_idx = lower.index('energy')

            for raw in f:
                if raw.strip() == '':
                    continue
                cols = parse_csv_line(raw)
                if max(name_idx, energy_idx) >= len(cols):
                    continue
                title = cols[name_idx]
                energy_str = cols[energy_idx]
                try:
                    energy = float(energy_str)
                except ValueError:
                    continue
                if min_energy <= energy <= max_energy:
                    print(title)
    except FileNotFoundError:
        print("File not found:", file_path)


# Interactive run (no imports): prompt the user for values using built-ins only
if __name__ == "__main__":
    default_path = r'C:\Users\jinas\Downloads\taylor_discography.csv'
    raw_path = input(f"CSV path [default: {default_path}]: ").strip()
    csv_path = raw_path if raw_path else default_path

    raw_min = input("Min energy (0.0-1.0) [default: 0.5]: ").strip()
    raw_max = input("Max energy (0.0-1.0) [default: 0.7]: ").strip()
    try:
        min_e = float(raw_min) if raw_min else 0.5
        max_e = float(raw_max) if raw_max else 0.7
    except Exception:
        print("Invalid numeric input; using defaults 0.5 and 0.7")
        min_e, max_e = 0.5, 0.7

    print_songs_in_energy_range(csv_path, min_e, max_e)
    
    # Prompt user for CSV path. Accept three forms:
    # 1) blank -> try local 'taylor_discography.csv' in cwd, else use default_path
    # 2) a direct path string
    # 3) a pasted call like: print_songs_in_energy_range(r'C:\path\file.csv', 0.4, 0.8)
    raw_path = input(f"CSV path [default: {default_path}]: ").strip()

    # If user pasted a function-like call, try to extract arguments
    csv_path = None
    min_e = None
    max_e = None
    if raw_path.startswith("print_songs_in_energy_range") and '(' in raw_path and ')' in raw_path:
        try:
            inner = raw_path[raw_path.find('(')+1:raw_path.rfind(')')]
            parts = [p.strip() for p in inner.split(',')]
            # path is the first argument; strip quotes and r prefix if present
            rawfile = parts[0]
            if rawfile.startswith('r') or rawfile.startswith('R'):
                rawfile = rawfile[1:]
            rawfile = rawfile.strip()
            if rawfile.startswith(('"', "'")) and rawfile.endswith(('"', "'")):
                rawfile = rawfile[1:-1]
            csv_path = rawfile
            if len(parts) >= 3:
                try:
                    min_e = float(parts[1])
                except Exception:
                    min_e = None
                try:
                    max_e = float(parts[2])
                except Exception:
                    max_e = None
        except Exception:
            csv_path = None

    # If not a pasted call, but user entered a raw path, use it
    if csv_path is None:
        if raw_path:
            csv_path = raw_path
        else:
            # try to find a local copy in the current working directory
            try:
                f = open('taylor_discography.csv', 'r', encoding='utf-8')
                f.close()
                csv_path = 'taylor_discography.csv'
                print("Using local file: taylor_discography.csv")
            except Exception:
                csv_path = default_path

    # Prompt for min/max only if not provided by pasted call
    if min_e is None or max_e is None:
        raw_min = input("Min energy (0.0-1.0) [default: 0.5]: ").strip()
        raw_max = input("Max energy (0.0-1.0) [default: 0.7]: ").strip()
        try:
            min_e = float(raw_min) if raw_min else (min_e if min_e is not None else 0.5)
            max_e = float(raw_max) if raw_max else (max_e if max_e is not None else 0.7)
        except Exception:
            print("Invalid numeric input; using defaults 0.5 and 0.7")
            min_e, max_e = 0.5, 0.7

    print_songs_in_energy_range(csv_path, min_e, max_e)
# Example usage (commented out):
# print_songs_in_energy_range(r'C:\Users\jinas\Downloads\taylor_discography.csv', 0.5, 0.7)


#click run, hit enter for CSV path, input min, input max, hit enter
