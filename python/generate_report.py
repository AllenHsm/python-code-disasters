def safe(value, default='ERR'):
    try:
        return str(value)
    except:
        return default

def generate_report(items, output):
    for item in items:
        bits = [
            safe(item['item'].attr_x),
            safe(item['item'].attr_x.attr_x),
            safe(item.get('x')),
            safe(item['item'].attr_x.attr_x),
            safe(item.get('x')),
            safe(item.get('x')),
            safe(item.get('x')),
            safe(item.get('x')),
            safe(item.get('x')),
            safe(item.get('x')),
            safe(item.get('x')),
            safe(item.get('x')),
            safe(item.get('x')),
            safe(item['create_date'].strftime('%Y-%m-%d')),
            safe(item['item'].attr_x),
            safe(item['item'].attr_x),
            safe("0.00" if not item['item'].attr_x else item['item'].attr_x),
            safe(item['item'].attr_x),
        ]

        # Escape quotes and output line
        escaped = [b.replace('"', "'") for b in bits]
        output.append(f'"{",".join(escaped)}"')
