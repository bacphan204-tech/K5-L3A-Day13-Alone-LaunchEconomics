"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py (cần pandas).
Không cần khoá API. Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k is None and p == 0:
        return math.inf
    if p == 0:
        return float(k)
    return ti_le_thanh_cong(p, k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return float(p > 0)
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return 1 / p if p > 0 and k != 0 else math.inf


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs.request_id.isin(reqs.request_id)]
    if max_lan_chay is not None:
        runs = runs[runs.attempt <= max_lan_chay]
        vuot = reqs.so_lan_chay > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    token = (runs.tokens_in * gia_vao + runs.tokens_out * gia_ra) / 1000
    tool = runs.tool_calls * gia_tool
    xem_lai = reqs.phut_xem_lai_simulated.sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs.phut_lam_lai_simulated.sum() * luong_phut * he_so_lam_lai
    tong = token.sum() + tool.sum() + xem_lai + lam_lai
    thanh_cong = reqs.ket_qua.eq('thanh_cong').sum()
    return dict(token=token.sum(), tool=tool.sum(),
                chay_lai=(token + tool)[runs.attempt > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong if thanh_cong else math.inf,
                hoa_don_moi_yc=(token.sum() + tool.sum()) / len(reqs) if len(reqs) else 0)


def co_mau(p1, p2, alpha=0.05, power=0.80):
    """Cỡ mẫu mỗi nhánh cho kiểm định hai phía với hai tỉ lệ."""
    z_alpha = NormalDist().inv_cdf(1 - alpha / 2)
    z_power = NormalDist().inv_cdf(power)
    trung_binh = (p1 + p2) / 2
    sai_so_goc = math.sqrt(2 * trung_binh * (1 - trung_binh))
    sai_so_doi = math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    return math.ceil(((z_alpha * sai_so_goc + z_power * sai_so_doi) / (p2 - p1)) ** 2)


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')

    print('\nA3: loại, yêu cầu, % thành công, lượt/yêu cầu, CPS, CPS/baseline')
    for loai, nhom in reqs.groupby('loai'):
        so = mo_hinh(runs, nhom)
        print(loai, len(nhom), f"{so['thanh_cong'] / len(nhom):.2%}",
              f'{nhom.so_lan_chay.mean():.2f}', f"{so['cps']:.2f}", f"{so['cps'] / BASELINE:.2f}")
    quoc_te = runs[runs.request_id.isin(reqs.loc[reqs.loai.eq('quoc_te'), 'request_id'])]
    print('Quốc tế: tỉ lệ OK theo lượt', quoc_te.status.eq('ok').groupby(quoc_te.attempt).mean().to_dict())

    pham_vi = reqs[reqs.loai.isin(['noi_dia', 'hang_nang'])]
    so_pilot = mo_hinh(runs, pham_vi)
    print('\nA4: yêu cầu/tháng, thành công, cố định/việc, CPS có cố định')
    for khoi_luong in (45000, 22500):
        thanh_cong = khoi_luong * so_pilot['thanh_cong'] / len(reqs)
        co_dinh = 40_000_000 / thanh_cong
        print(khoi_luong, thanh_cong, round(co_dinh, 2), round(so_pilot['cps'] + co_dinh, 2))
    hoa_von = 40_000_000 / (BASELINE - so_pilot['cps']) / (so_pilot['thanh_cong'] / len(reqs))
    print('Khối lượng hòa vốn:', math.ceil(hoa_von))

    kich_ban = {
        'Token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Token giảm nửa': dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi': dict(he_so_xem_lai=2),
        'Xem lại giảm nửa': dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi': dict(he_so_lam_lai=2),
        'Làm lại giảm nửa': dict(he_so_lam_lai=0.5),
        'Lương tăng 25%': dict(luong_phut=2500),
        'Tối đa 2 lần': dict(max_lan_chay=2),
        'Tối đa 1 lần': dict(max_lan_chay=1),
        'Token và xem lại gấp đôi (B2)': dict(gia_vao=52, gia_ra=260, he_so_xem_lai=2),
    }
    print('\nB1–B2: kịch bản, CPS, thay đổi')
    for ten, tham_so in kich_ban.items():
        cps = mo_hinh(runs, reqs, **tham_so)['cps']
        print(f'{ten:30s} {cps:9.2f} {cps / ket_qua["cps"] - 1:+.2%}')

    print('\nB3: giới hạn, chi phí trợ lý, ca thất bại, chi phí hệ thống, CPS')
    for gioi_han in (1, 2, 3):
        so = mo_hinh(runs, reqs, max_lan_chay=gioi_han)
        that_bai = len(reqs) - so['thanh_cong']
        chi_phi_he_thong = so['tong'] + BASELINE * that_bai
        print(gioi_han, round(so['tong'], 2), that_bai, round(chi_phi_he_thong, 2), round(so['cps'], 2))

    so_xem_lai = runs.loc[runs.request_id.isin(pham_vi.request_id) & runs.status.eq('ok'), 'request_id'].nunique()
    lam_lai = reqs.loc[reqs.ket_qua.eq('lam_lai'), 'phut_lam_lai_simulated']
    so_lam_lai = pham_vi.ket_qua.eq('lam_lai').sum()
    print('\nB4: phút làm lại/ca, CPS xem lại 100%, phút xem lại hòa vốn')
    for phut in (9, round(lam_lai.mean(), 1)):
        chi_phi_khac = so_pilot['token'] + so_pilot['tool'] + so_lam_lai * phut * LUONG_PHUT
        cps = (chi_phi_khac + so_xem_lai * 5 * LUONG_PHUT) / so_pilot['thanh_cong']
        phut_hoa_von = (BASELINE * so_pilot['thanh_cong'] - chi_phi_khac) / (so_xem_lai * LUONG_PHUT)
        print(phut, round(cps, 2), round(phut_hoa_von, 2))

    icc = 0.02
    n_5 = co_mau(0.70, 0.75)
    de = 1 + (75 - 1) * icc
    n_cum = math.ceil(n_5 * de)
    n_6 = 859  # Mức đề bài cho sẵn cho câu D1e.
    m = math.ceil(n_6 * (1 - icc) / (20 - n_6 * icc))
    print('\nD1:', n_5, de, n_cum, math.ceil(n_cum / 75), 20 / icc, 6 / icc, m)
    print('D1e: yêu cầu thực và hiệu dụng mỗi nhánh:', 20 * m, 20 * m / (1 + (m - 1) * icc))

    da_xem_lai = reqs[reqs.duoc_xem_lai.eq(1)]
    print('\nE1: đạt chỉ số chính, sửa/bỏ, mở lại, mở lại trong phạm vi')
    print((reqs.dong_trong_24h.eq(1) & reqs.mo_lai_trong_7_ngay.eq(0)).sum(), '/', len(reqs))
    print(da_xem_lai.quyet_dinh_xem_lai.isin(['sua', 'bo']).sum(), '/', len(da_xem_lai))
    print(reqs.mo_lai_trong_7_ngay.sum(), '/', len(reqs))
    print(pham_vi.mo_lai_trong_7_ngay.sum(), '/', len(pham_vi))
