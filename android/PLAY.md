# HomeRx — Google Play build

Free app. Application ID `com.hakoya.homerx`. Publisher: HAKOYA LLC.

The Google Play build is `scripts/build-store.py` run on the repository's `index.html`. The web
app is not modified: it already works offline (system fonts, no external scripts or stylesheets,
no network calls, no service worker, no file downloads), so the store bundle is the web app plus a
build marker and its local icon and manifest files. The build fails if the source gains a network
request, a service worker or a file download, or loses EN/KO/JA parity on any entry or UI string;
handle the new case in `build-store.py` before the next store build.

Content in this build (from `index.html` on the built commit): 71 entries (48 OTC + 23
supplements), English / Korean / Japanese on every field.

The app uses no Capacitor plugins. The manifest requests only `INTERNET`, which Capacitor's
template declares for its local web server; the app makes no network request.

## Build
GitHub Actions → "Android build (Google Play)". Runs on a push to `android-build` or by manual
dispatch. Produces an **unsigned** App Bundle, kept as a workflow artifact and committed to the
`android-artifacts` branch at `dist/homerx-<version>-<code>-unsigned.aab` (`dist/LATEST` names
the newest). versionCode = workflow run number.

Local check of the web bundle:

    cd android && npm ci && npm run build:www
    python3 -m http.server -d www 8000

## Sign
HAKOYA LLC upload key (same key as TOXCARD and Silent Medic Vet; kept by the account holder,
backed up in Google Drive 00_CLAUDE_HQ/TOXCARD_Android_UploadKey):

    jarsigner -keystore toxcard-upload.jks -signedjar out-signed.aab in-unsigned.aab toxcard-upload
    jarsigner -verify out-signed.aab

## Files
- `scripts/build-store.py` — store web bundle (android/www) from index.html, with offline and parity checks
- `scripts/native-setup.py` — launcher and adaptive icons, splash, version, ID, targetSdk and permission checks
- `capacitor.config.json`, `package.json`, `package-lock.json`
- `listing/` — Play Console listing text, Data safety, content rating, Health apps declaration, graphics
