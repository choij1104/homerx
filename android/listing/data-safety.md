# HomeRx — Data safety form (Play Console → App content → Data safety)

Basis, checked in the built bundle and the AAB:
- index.html makes no network request (no fetch/XHR/WebSocket/beacon, no external script, font,
  stylesheet or image). build-store.py fails the build if one is added.
- v2 keeps the cabinet (product list and expiry dates), ticked health conditions, language, text
  size and notice confirmation in the WebView's localStorage on the device only (key prefix
  `homerx2.`). Nothing is transmitted, so under Play's definition this is not "collected"
  (data processed only on the device is not collection). Uninstalling or clearing app data removes it.
- No analytics, crash reporting, ads or third-party SDKs. The app uses no Capacitor plugins.
- AndroidManifest permissions: `INTERNET` only (declared by Capacitor's template for its local
  web server). No location, camera, contacts, storage, phone or account permissions.
- Playwright test of the store build in EN/KO/JA: zero requests to any host other than the local
  test server.

## Answers

| Question | Answer |
|---|---|
| Does your app collect or share any of the required user data types? | **No** |
| Is all of the user data collected by your app encrypted in transit? | Not shown (no data collected) |
| Do you provide a way for users to request that their data is deleted? | Not shown (no data collected) |

Result shown on Google Play: **"No data collected"** and **"No data shared with third parties"**.

## Security practices (optional badges)
- Independent security review: No
- Committed to Play Families Policy: not applicable (not designed for children; audience 18+)

## Note
If a future version adds analytics, crash reporting, accounts, saved favourites synced to a
server, or any network call, this form must be updated before that version is released.
