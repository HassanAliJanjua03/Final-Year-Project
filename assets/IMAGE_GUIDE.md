# Editing my project pictures

The main README uses ordinary image links and HTML image tags. The layout, technical text and diagrams can stay exactly as they are while the photos are changed.

## 1. Upload a picture

Open [assets/images](images), choose **Add file → Upload files**, select a PNG, JPG or WebP, and commit it to the main branch (or open a pull request if preferred). Use short lowercase names with underscores, e.g. `esp32_setup.jpg`.

## 2. Add it to the main README

Open [README.md](../README.md) and click the pencil icon. Search for `IMAGE SECTION:` to locate the relevant image area. Paste this line on its own, outside existing HTML tables, to add a picture:

```markdown
![ESP32 data acquisition setup](assets/images/esp32_setup.jpg)
```

This is a template; upload the named picture first or change the filename to the one you actually uploaded.

For a centered picture with a caption:

```html
<p align="center">
  <a href="assets/images/esp32_setup.jpg">
    <img src="assets/images/esp32_setup.jpg" alt="ESP32 data acquisition setup" width="700">
  </a>
  <br><em>My ESP32 data acquisition setup</em>
</p>
```

Use the **Preview** tab before committing.

## 3. Replace an existing picture

The current photos are under [previews](previews). Upload your new picture to images, then search for the old path in README.md. For example, replace BOTH occurrences of `assets/previews/solidworks_assembly.webp` in the link and image tag with `assets/images/my_new_cad.png`. Keep the surrounding HTML to preserve the layout. Update the matching gallery link in [assets/README.md](README.md) too, using paths relative to that file (e.g. `images/my_new_cad.png`).

Alternatively, upload a replacement with exactly the same filename, extension and folder as the current image; all existing references will keep working. Do not rename a PNG or JPG to .webp without converting it.

## 4. Remove a picture

Delete the complete standalone image line or its complete centered paragraph. In a two-column table, remove only the linked image and caption from its cell, or remove the whole table if you no longer want that pair. Do not delete the file itself until all references to it have been removed from the README and gallery.

## Current image locations

| Section | Current image filename in assets/previews |
| --- | --- |
| Top gallery — physical robot | physical_prototype.webp |
| Top gallery — Unity | unity_digital_twin.webp |
| Mechanical design | solidworks_assembly.webp |
| Hardware | hardware_overview.webp |
| Modeling & control | modeling_overview.webp |
| Kinematics | inverse_kinematics_trajectory.webp |
| Data Acquisition | influxdb_overview.webp |
| Data Acquisition | grafana_dashboard.webp |

The graphics in assets/design and docs/architecture.svg are separate from the project photos. Leave those files unchanged to retain the current visual design.

[Back to gallery](README.md) · [Back to project](../README.md)
