try:
    from products.serializers import ProductSerializer
    print("Import thành công ProductSerializer!")
except ImportError as e:
    print("Lỗi Import:", e)
