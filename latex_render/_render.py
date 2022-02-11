from selenium import webdriver
from pathlib import Path
from PIL import Image
from io import BytesIO
import json
from time import sleep
from base64 import b64encode

file = Path(__file__).parent / "site" / "page.html"


def autocrop_image(image, border=0):
    bbox = image.getbbox()
    image = image.crop(bbox)
    (width, height) = image.size

    width += border * 2
    height += border * 2

    cropped_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    cropped_image.paste(image, (border, border))

    return cropped_image


def render(latex, font_size=24, color="black", border=8):
    options = webdriver.ChromeOptions()
    options.add_argument("--force-device-scale-factor=1.0")
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.command_executor._request(
        "POST",
        driver.command_executor._url
        + "/session/%s/chromium/send_command_and_get_result" % driver.session_id,
        json.dumps(
            {
                "cmd": "Emulation.setDefaultBackgroundColorOverride",
                "params": {"color": {"r": 0, "g": 0, "b": 0, "a": 0}},
            }
        ),
    )

    driver.get(file.as_uri())

    driver.execute_script(
        f"document.body.style.fontSize = '{font_size}px'; document.body.style.color = '{color}'"
    )
    toSetLatex = f'katex.render(String.raw`{latex}`, document.querySelector("#math-render-target"), {{displayMode: true}})'
    driver.set_window_size(1000, 1000)
    driver.execute_script(toSetLatex)

    sleep(0.02)

    image = driver.find_element_by_id("math-render-target").screenshot_as_png
    driver.close()

    new_img = Image.open(BytesIO(image))
    return autocrop_image(new_img, border)


def render_to_file(latex, file, font_size=24, color="black", border=8):
    img = render(latex, font_size, color, border)
    img.save(file)

def render_as_uri(latex, font_size=24, color="black", border=8):
    img = render(latex, font_size, color, border)
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    return "data:image/png;base64," + b64encode(buffer.getvalue()).decode("ascii")