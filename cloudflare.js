/*
    Default Addon for CloudFlare
    
    
*/


const colors = require('colors');

function log(string) {
    let d = new Date();
    let hours = (d.getHours() < 10 ? '0' : '') + d.getHours();
    let minutes = (d.getMinutes() < 10 ? '0' : '') + d.getMinutes();
    let seconds = (d.getSeconds() < 10 ? '0' : '') + d.getSeconds();
    console.log(`(${hours}:${minutes}:${seconds})`.white + ` - ${string}`);
}

async function captchaSolver(page, context, response) {
    log(`(${'CLOUDFLARE-CKDDOSV5'.green}) Detected protection -> ` + `CloudFlare (JS)`.green);

    for (let i = 0; i < 15; i++) {
        (async () => {
            await page.waitForTimeout(1000);
            await page.mouse.move(randomIntFromInterval(10, 230), randomIntFromInterval(10, 230))
        })
    }

    if (await page.title() === "Just a moment...") {
        const hcaptcha_box = await page.locator('//*[@id="turnstile-wrapper"]/div');   // Looking for captcha button

        if (hcaptcha_box) {
            let x;
            let y;
            let captchaDetect = false;

            try {
                const rect = await hcaptcha_box.boundingBox();
                x = rect.x + rect.width / 2;
                y = rect.y + rect.height / 2;

                log(`(${'CLOUDFLARE-CKDDOSV5'.green}) Managed challenge -> ` + `Detected captcha`.green);
                log(`(${'CLOUDFLARE-CKDDOSV5'.green}) Detected element -> ` + `[ captcha box ]`.green);

                captchaDetect = true;
            } catch (e) {
                log(`(${'CLOUDFLARE-CKDDOSV5'.green}) Managed challenge -> ` + `UAM`.green);
                await page.waitForTimeout(15000);

                if (await page.title() === "Just a moment...") {
                    await page.waitForTimeout(15000);


                    if (await page.title() === "Just a moment...") {
                        await page.waitForTimeout(15000);
                    }
                }
            }

            if (captchaDetect) {
                await page.mouse.click(x, y);

                log(`(${'CLOUDFLARE-CKDDOSV5'.green}) Element clicked -> ` + `[ captcha box ]`.green);

                await page.waitForTimeout(10000);

                if (await page.title() === "Just a moment...") {
                    await page.waitForTimeout(3000);
                    await page.mouse.click(x, y);
                    log(`(${'CLOUDFLARE-CKDDOSV5'.green}) Element clicked -> ` + `[ captcha box ]`.green);
                    await page.waitForTimeout(10000);

                    if (await page.title() === "Just a moment...") {
                        await page.waitForTimeout(3000);
                        await page.mouse.click(x, y);
                        log(`(${'CLOUDFLARE-CKDDOSV5'.green}) Element clicked -> ` + `[ captcha box ]`.green);
                        await page.waitForTimeout(10000);

                        if (await page.title() === "Just a moment...") {
                            await page.waitForTimeout(3000);
                            await page.mouse.click(x, y);
                            log(`(${'CLOUDFLARE-CKDDOSV5'.green}) Element clicked -> ` + `[ captcha box ]`.green);
                            await page.waitForTimeout(10000);

                            if (await page.title() === "Just a moment...") {
                                await page.waitForTimeout(3000);
                                await page.mouse.click(x, y);
                                log(`(${'CLOUDFLARE-CKDDOSV5'.green}) Element clicked -> ` + `[ captcha box ]`.green);
                                await page.waitForTimeout(10000);

                                if (await page.title() === "Just a moment...") {
                                    await page.waitForTimeout(3000);
                                    await page.mouse.click(x, y);
                                    log(`(${'CLOUDFLARE-CKDDOSV5'.green}) Element clicked -> ` + `[ captcha box ]`.green);
                                    await page.waitForTimeout(10000);

                                    if (await page.title() === "Just a moment...") {
                                        await page.waitForTimeout(3000);
                                        await page.mouse.click(x, y);
                                        log(`(${'CLOUDFLARE-CKDDOSV5'.green}) Element clicked -> ` + `[ captcha box ]`.green);
                                        await page.waitForTimeout(10000);

                                        if (await page.title() === "Just a moment...") {
                                            await page.waitForTimeout(3000);
                                            await page.mouse.click(x, y);
                                            log(`(${'CLOUDFLARE-CKDDOSV5'.green}) Element clicked -> ` + `[ captcha box ]`.green);
                                            await page.waitForTimeout(10000);

                                            if (await page.title() === "Just a moment...") {
                                                await page.waitForTimeout(3000);
                                                await page.mouse.click(x, y);
                                                log(`(${'CLOUDFLARE-CKDDOSV5'.green}) Element clicked -> ` + `[ captcha box ]`.green);
                                                await page.waitForTimeout(10000);

                                                if (await page.title() === "Just a moment...") {
                                                    await page.waitForTimeout(3000);
                                                    await page.mouse.click(x, y);
                                                    log(`(${'CLOUDFLARE-CKDDOSV5'.green}) Element clicked -> ` + `[ captcha box ]`.green);
                                                    await page.waitForTimeout(10000);
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    } else {
        log(`(${'CLOUDFLARE-CKDDOSV5'.green}) Managed challenge -> ` + `UAM`.green);
        await page.waitForTimeout(15000);
    }

    const title = await page.title();
    const cookies = (await context.cookies()).map(c => `${c.name}=${c.value}`).join('; ');
    const headers = await response.request().allHeaders();
    const headerEntries = Object.entries(headers);

    return [title, cookies, headerEntries];
}

function initialize() { }

module.exports = {
    initialize: initialize,
    captchaSolver: captchaSolver
};