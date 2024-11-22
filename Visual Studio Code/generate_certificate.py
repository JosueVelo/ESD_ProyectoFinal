from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.x509 import (
    CertificateBuilder,
    CertificateSigningRequestBuilder,
    Name,
    NameAttribute,
    BasicConstraints,
    random_serial_number,
    NameOID
)
from datetime import datetime, timedelta, timezone
import getpass

def generate_certificate():
    # Generar clave privada
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    # Solicitar contraseña para proteger la clave privada
    password = getpass.getpass("Introduce una contraseña para proteger la clave privada: ")

    # Guardar la clave privada cifrada
    private_key_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.BestAvailableEncryption(password.encode())
    )

    with open("private_key.pem", "wb") as f:
        f.write(private_key_bytes)

    # Crear una CSR
    csr = CertificateSigningRequestBuilder().subject_name(
        Name([
            NameAttribute(NameOID.COMMON_NAME, "SalaryBoost.com.pe"),  # Cambia esto a tu dominio si es necesario
        ])
    ).sign(private_key, hashes.SHA256(), default_backend())

    # Guardar la CSR
    with open("certificate_request.csr", "wb") as f:
        f.write(csr.public_bytes(serialization.Encoding.PEM))

    # Crear un certificado auto-firmado
    certificate = (
        CertificateBuilder()
        .subject_name(csr.subject)
        .issuer_name(csr.subject)  # Para auto-firmado
        .public_key(csr.public_key())
        .serial_number(random_serial_number())
        .not_valid_before(datetime.now(timezone.utc))  # Usar datetime con zona horaria
        .not_valid_after(datetime.now(timezone.utc) + timedelta(days=365))  # Válido por 1 año
        .add_extension(BasicConstraints(ca=False, path_length=None), critical=True)  # Agregar path_length
        .sign(private_key, hashes.SHA256(), default_backend())
    )

    # Guardar el certificado
    with open("certificate.crt", "wb") as f:
        f.write(certificate.public_bytes(serialization.Encoding.PEM))

    print("Certificado y clave privada generados con éxito.")

if __name__ == "__main__":
    generate_certificate()
