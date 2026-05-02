const fs = require('fs');

let content = fs.readFileSync('index.html', 'utf8');

// 1. Fix hero badge text
content = content.replace(
  /<span data-ar="HAARLEM • BERNADOTTELAAN 3A •"[^>]*>HAARLEM • BERNADOTTELAAN 3A •<\/span>/g,
  '<span data-ar="HAARLEM" data-nl="HAARLEM" style="letter-spacing: 1px; font-weight: 800;">HAARLEM</span>'
);

// 2. Add product numbers
let productCounter = 1;
content = content.replace(/<div class="product-img-wrap"([^>]*)>/g, (match, p1) => {
  const numberHtml = `\n        <span style="position: absolute; top: 0.75rem; right: 0.75rem; background: rgba(0,0,0,0.6); color: #fff; padding: 0.2rem 0.5rem; border-radius: 6px; font-size: 0.7rem; font-weight: 900; z-index: 2;">#${String(productCounter).padStart(3, '0')}</span>`;
  productCounter++;
  return match + numberHtml;
});

// 3. Add discount to Strawberries
const strawberriesPattern = /<h3 data-ar="فراولة"[^>]*>فراولة<\/h3>\s*<div class="product-price">\s*<span class="price-label"[^>]*>.*?<\/span>\s*<span class="price-value">€2.99<\/span>\s*<\/div>/g;
const strawberriesReplacement = `<h3 data-ar="فراولة" data-nl="Aardbeien">فراولة</h3>
        <div class="product-price">
          <span class="price-label" data-ar="خصم" data-nl="Korting" style="color: #e74c3c; font-weight: bold;">خصم</span>
          <div style="display:flex; align-items:center; gap:0.4rem;">
            <span class="price-value" style="text-decoration: line-through; color: #888; font-size: 0.85rem;">€3.99</span>
            <span class="price-value" style="color: #e74c3c;">€2.99</span>
          </div>
        </div>`;
content = content.replace(strawberriesPattern, strawberriesReplacement);

// Add discount to Makdous
const makdousPattern = /<h3 data-ar="مكدوس"[^>]*>مكدوس<\/h3>\s*<div class="product-price">\s*<span class="price-label"[^>]*>.*?<\/span>\s*<span class="price-value">€7.99<\/span>\s*<\/div>/g;
const makdousReplacement = `<h3 data-ar="مكدوس" data-nl="Makdous">مكدوس</h3>
        <div class="product-price">
          <span class="price-label" data-ar="خصم" data-nl="Korting" style="color: #e74c3c; font-weight: bold;">خصم</span>
          <div style="display:flex; align-items:center; gap:0.4rem;">
            <span class="price-value" style="text-decoration: line-through; color: #888; font-size: 0.85rem;">€9.99</span>
            <span class="price-value" style="color: #e74c3c;">€7.99</span>
          </div>
        </div>`;
content = content.replace(makdousPattern, makdousReplacement);

// 4. Update WhatsApp floating icon
const waFloatPattern = /<a class="float-btn float-wa"[^>]*>💬<\/a>/;
const waSvg = `<a class="float-btn float-wa" href="https://wa.me/31617711223" target="_blank" title="WhatsApp" style="display:flex; justify-content:center; align-items:center;">
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 16 16">
      <path d="M13.601 2.326A7.85 7.85 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c-.003 1.396.366 2.76 1.057 3.965L0 16l4.204-1.102a7.9 7.9 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.9 7.9 0 0 0 13.6 2.326zM7.994 14.521a6.6 6.6 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.56 6.56 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592m3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.007-.247-.007-.38-.007a.73.73 0 0 0-.529.247c-.182.198-.691.677-.691 1.654s.71 1.916.81 2.049c.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232"/>
    </svg>
  </a>`;
content = content.replace(waFloatPattern, waSvg);

fs.writeFileSync('index.html', content);
console.log('Update successful!');
