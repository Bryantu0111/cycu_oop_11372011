import asyncio
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

async def find_bus_route():
    start_station = input("請輸入起始站牌名稱：").strip()
    destination_station = input("請輸入目的地站牌名稱：").strip()
    url = "https://ebus.gov.taipei/ebus"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)  # 啟用無頭模式
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )
        page = await context.new_page()
        await page.goto(url)

        # 添加延遲，確保動態內容加載完成
        await page.wait_for_timeout(5000)  # 等待 5 秒

        try:
            await page.wait_for_selector("div.route-list", timeout=60000)  # 等待目標元素加載
        except Exception as e:
            print(f"網頁載入超時，錯誤訊息：{e}")
            await browser.close()
            return

        html = await page.content()
        await browser.close()

    soup = BeautifulSoup(html, "html.parser")
    route_items = soup.select("div.route-list a")

    if not route_items:
        print("未找到任何公車路線資訊，請稍後再試。")
        return

    all_routes = []

    for route in route_items:
        try:
            route_name = route.get_text(strip=True)
            route_url = route["href"]
            all_routes.append({"name": route_name, "url": route_url})
        except Exception as e:
            print(f"處理路線時發生錯誤：{e}")

    if not all_routes:
        print("沒有成功抓取到任何公車路線資訊。")
        return

    suggested_routes = []

    for route in all_routes:
        try:
            route_page_url = f"https://ebus.gov.taipei{route['url']}"
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=True)  # 啟用無頭模式
                context = await browser.new_context()
                page = await context.new_page()
                await page.goto(route_page_url)

                try:
                    await page.wait_for_selector("div#GoDirectionRoute li", timeout=60000)  # 增加超時時間
                except:
                    continue

                route_html = await page.content()
                await browser.close()

            route_soup = BeautifulSoup(route_html, "html.parser")
            station_items = route_soup.select("div#GoDirectionRoute li")

            # 提取站牌名稱和到站時間
            station_data = []
            for li in station_items:
                try:
                    stop_name = li.select_one("span.auto-list-stationlist span:nth-child(3)").get_text(strip=True)
                    stop_time = li.select_one("span.auto-list-stationlist span:nth-child(1)").get_text(strip=True)
                    station_data.append({"name": stop_name, "time": stop_time})
                except Exception as e:
                    continue

            # 檢查是否包含起始站和目的地站
            station_names = [station["name"] for station in station_data]
            if start_station in station_names and destination_station in station_names:
                start_index = station_names.index(start_station)
                destination_index = station_names.index(destination_station)

                if start_index < destination_index:  # 確保方向正確
                    suggested_routes.append({
                        "name": route["name"],
                        "start_time": station_data[start_index]["time"],
                        "destination_time": station_data[destination_index]["time"]
                    })

        except Exception as e:
            print(f"處理路線 {route['name']} 時發生錯誤：{e}")

    if suggested_routes:
        print("\n建議搭乘的公車路線如下：")
        for route in suggested_routes:
            print(f"- 路線名稱: {route['name']}")
            print(f"  起始站 {start_station} 到站時間: {route['start_time']}")
            print(f"  目的地站 {destination_station} 到站時間: {route['destination_time']}")
    else:
        print("\n未找到包含起始站和目的地站的公車路線，請確認站牌名稱是否正確。")

if __name__ == "__main__":
    asyncio.run(find_bus_route())