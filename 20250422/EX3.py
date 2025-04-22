import json
import matplotlib.pyplot as plt

def get_station_coordinates(geojson_path, station_names):
    """
    從 GeoJSON 檔案中提取指定車站名稱的經緯度。
    :param geojson_path: GeoJSON 檔案路徑
    :param station_names: 車站名稱列表
    :return: 車站名稱與經緯度的對應字典
    """
    with open(geojson_path, "r", encoding="utf-8") as f:
        geojson_data = json.load(f)

    station_coordinates = {}
    for feature in geojson_data["features"]:
        properties = feature["properties"]
        geometry = feature["geometry"]
        station_name = properties.get("name")  # 假設車站名稱在 "name" 欄位
        if station_name in station_names:
            station_coordinates[station_name] = geometry["coordinates"]

    return station_coordinates

def plot_routes(station_coordinates, route_name, color):
    """
    繪製路線圖。
    :param station_coordinates: 車站名稱與經緯度的對應字典
    :param route_name: 路線名稱
    :param color: 路線顏色
    """
    lons, lats = zip(*station_coordinates.values())
    plt.plot(lons, lats, marker="o", label=route_name, color=color)
    for station, (lon, lat) in station_coordinates.items():
        plt.text(lon, lat, station, fontsize=8, ha="right")

def main():
    # 承德幹線與基隆幹線的車站名稱
    chengde_stations = ["Station A", "Station B", "Station C"]  # 替換為實際車站名稱
    keelung_stations = ["Station X", "Station Y", "Station Z"]  # 替換為實際車站名稱

    # GeoJSON 檔案路徑
    geojson_path = "C:\\Users\\User\\Desktop\\cycu_oop_11372011\\20250422\\bus_stations.geojson"

    # 獲取車站經緯度
    chengde_coordinates = get_station_coordinates(geojson_path, chengde_stations)
    keelung_coordinates = get_station_coordinates(geojson_path, keelung_stations)

    # 繪製路線圖
    plt.figure(figsize=(10, 8))
    plot_routes(chengde_coordinates, "承德幹線", "blue")
    plot_routes(keelung_coordinates, "基隆幹線", "red")

    # 圖例與標題
    plt.legend()
    plt.title("承德幹線與基隆幹線車站路線圖")
    plt.xlabel("經度")
    plt.ylabel("緯度")
    plt.grid(True)

    # 儲存圖片
    output_path = "C:\\Users\\User\\Desktop\\cycu_oop_11372011\\20250422\\bus_routes.png"
    plt.savefig(output_path)
    plt.show()
    print(f"路線圖已儲存為 {output_path}")

if __name__ == "__main__":
    main()