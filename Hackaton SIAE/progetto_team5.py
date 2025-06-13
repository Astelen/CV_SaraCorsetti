# 'Data Talent Challenge' 23 Maggio 2025, SIAE.
# Background: gli accertatori della SIAE devono recarsi nei locali per ritirare le quote per i diritti d'autore.
# Il nostro compito era ideare un algoritmo per massimizzare il guadagno, selezionando i locali che hanno una quota piu' alta.
# Ogni giornata lavorativa consisteva in 3 ore di lavoro ed un massimo di 8 locali visitabili dagli accertatori.
# L'utilizzo delle API di Google Maps era limitato. Quindi abbiamo pensato ad un approccio diverso:
# lavorare sulle distanze, sapendo che ogni 15 min si puo' percorrere circa 1 km, e massimo 12 km totali.
# Abbiamo quindi definito una distanza massima dal punto di inizio e una distanza radiale di 1 km dal punto di partenza,
# e da un punto all'altro.
# Abbiamo poi dato un punteggio ad ogni locale(/cliente):
# il punteggio era il rapporto tra quota e distanza dal punto precedente,
# per l'inverso della distanza dal punto di origine moltiplicato il numero progressivo della tappa.
# Abbiamo elevato questi due elementi a due coefficienti per ottimizzare il punteggio e quindi l'algoritmo.

# Codice: Francesco Zese, Sara Corsetti

import math
import pandas as pd

def haversine(coord1, coord2):
    R = 6371000  # raggio medio della Terra in metri
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi / 2) ** 2 + \
        math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

max_customers = 8
max_dist = 8000
search_radius = 1000
epsilon = 1e-6

df = pd.read_csv('finale.csv')
df_coord = pd.read_csv('coordinate_per_giorno.csv')
start_points = df_coord[['lat_x', 'lon_x']].values.tolist()
num_routes = len(start_points)

clients_original = []
for i, row in df.iterrows():
    clients_original.append({
        'id': int(i + 1),
        'coord': [row['lat_x'], row['lon_x']],
        'amount': row['fee_value'],
        'jurisdiction': row['jurisdiction'],
        'visited_global': False
    })

all_routes = []

for day in range(1, num_routes + 1):
    lat, lon = start_points[day-1][0], start_points[day-1][1]
    start_coord = [lat, lon]
    # Trova la giurisdizione più vicina nel dataset principale
    df['distance'] = ((df['lat_x'] - lat)**2 + (df['lon_x'] - lon)**2)
    start_jurisdiction = df.loc[df['distance'].idxmin()]['jurisdiction']
    route_id = f"R{start_jurisdiction}_{day}"
    print(f"\n[Percorso {day}] Punto di partenza: giurisdizione {start_jurisdiction}")

    # Parametri di ottimizzazione
    alpha = 1
    beta = 5
    alpha_growth_factor = 1.5
    beta_decay_factor = 1.5
    beta_min = 0.05

    best_route = []
    best_fee = -1
    best_distance = 0
    best_alpha = alpha
    best_beta = beta

    while beta >= beta_min:
        # Reset clienti
        clients = [dict(c) for c in clients_original]
        for c in clients:
            c['visited'] = False

        current_point = start_coord
        route = [{
            'route_id': route_id,
            'jurisdiction_id': start_jurisdiction,
            'stop_order': 1,
            'poi_id': 0,
            'lat': start_coord[0],
            'lon': start_coord[1],
            'estimated_fee_value': 0
        }]
        total_distance = 0
        stop_counter = 2

        for step in range(1, max_customers + 1):
            candidates = []
            for c in clients:
                if not c['visited'] and not c['visited_global'] and c['jurisdiction'] == start_jurisdiction:
                    dist = haversine(current_point, c['coord'])
                    if dist <= search_radius:
                        dist_to_depot = haversine(c['coord'], start_coord)
                        score = (c['amount']**alpha / (dist + epsilon)) * (1 / ((dist_to_depot + epsilon) ** (step * beta)))
                        candidates.append((c, dist, score))

            if not candidates:
                break

            selected, dist_to_selected, _ = max(candidates, key=lambda x: x[2])
            selected['visited'] = True
            route.append({
                'route_id': route_id,
                'jurisdiction_id': start_jurisdiction,
                'stop_order': stop_counter,
                'poi_id': selected['id'],
                'lat': selected['coord'][0],
                'lon': selected['coord'][1],
                'estimated_fee_value': selected['amount']
            })
            total_distance += dist_to_selected
            current_point = selected['coord']
            stop_counter += 1

        # Ritorno al deposito
        dist_back = haversine(current_point, start_coord)
        total_distance += dist_back
        route.append({
            'route_id': route_id,
            'jurisdiction_id': start_jurisdiction,
            'stop_order': stop_counter,
            'poi_id': 0,
            'lat': start_coord[0],
            'lon': start_coord[1],
            'estimated_fee_value': 0
        })

        total_fee = sum(stop['estimated_fee_value'] for stop in route)

        if total_distance <= max_dist and total_fee > best_fee:
            best_route = route
            best_fee = total_fee
            best_distance = total_distance
            best_alpha = alpha
            best_beta = beta

        alpha *= alpha_growth_factor
        beta /= beta_decay_factor

    # Marca i clienti visitati in questo percorso come 'visited_global'
    for stop in best_route:
        if stop['poi_id'] != 0:
            for c in clients_original:
                if c['id'] == stop['poi_id']:
                    c['visited_global'] = True

    # Invece di salvare ogni percorso, aggiungi a all_routes
    all_routes.extend(best_route)

    print(f"Distanza totale percorso: {best_distance:.2f} metri")
    print(f"Importo totale incassato: €{best_fee:.2f}")
    print(f"Valori finali ottimali -> alpha: {best_alpha:.3f}, beta: {best_beta:.3f}")

    print("\nCoordinate dei punti del percorso:")
    for stop in best_route:
        print(f"Cliente: {stop['stop_order']:>2} | Lat: {stop['lat']:.5f}, Lon: {stop['lon']:.5f}")

# Dopo il ciclo, salva tutto in un unico CSV
df_all = pd.DataFrame(all_routes)
df_all.to_csv('csv_submission_team5.csv', index=False)
print("\nFile unico salvato come: csv_submission_team5.csv")