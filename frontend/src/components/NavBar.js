import React from 'react';

/**
 * Shared NavBar component for uniform navigation across all pages.
 * 
 * Props:
 *   activePage    - 'home' | 'profile' | 'activity' (which tab to highlight)
 *   onNavigate    - function(page) called with 'home', 'profile', or 'activity'
 *   rightContent  - optional JSX to render on the right side of the nav
 */
function NavBar({ activePage = 'home', onNavigate, rightContent }) {
  const pages = [
    { key: 'home', label: 'Home' },
    { key: 'profile', label: 'Profile' },
    { key: 'activity', label: 'Activity' },
  ];

  return (
    <nav style={navStyles.navbar}>
      <div className="nav-container" style={navStyles.navContainer}>
        {/* Brand - clickable to go home */}
        <div style={navStyles.navBrand} onClick={() => onNavigate && onNavigate('home')}>
          <img src="/logo.png" alt="CoursePro" className="nav-logo" style={navStyles.navLogo} />
          <span className="nav-brand-text" style={navStyles.navBrandName}>CoursePro</span>
        </div>

        {/* Center tabs */}
        <div className="nav-links" style={navStyles.navLinks}>
          {pages.map((p) => (
            <span
              key={p.key}
              className="nav-link"
              style={
                activePage === p.key
                  ? { ...navStyles.navLink, ...navStyles.navLinkActive }
                  : navStyles.navLink
              }
              onClick={() => {
                if (activePage !== p.key && onNavigate) onNavigate(p.key);
              }}
            >
              {p.label}
            </span>
          ))}
        </div>

        {/* Right side */}
        <div style={navStyles.navRight}>
          {rightContent || null}
        </div>
      </div>
    </nav>
  );
}

const navStyles = {
  navbar: {
    position: 'sticky',
    top: 0,
    zIndex: 100,
    background: 'rgba(5, 5, 16, 0.85)',
    backdropFilter: 'blur(24px)',
    WebkitBackdropFilter: 'blur(24px)',
    borderBottom: '1px solid rgba(255, 255, 255, 0.04)',
    transition: 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)',
  },
  navContainer: {
    maxWidth: '1400px',
    margin: '0 auto',
    padding: '14px 40px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-between',
    position: 'relative',
  },
  navBrand: {
    display: 'flex',
    alignItems: 'center',
    gap: '14px',
    zIndex: 1,
    cursor: 'pointer',
  },
  navLogo: {
    width: '48px',
    height: '48px',
    objectFit: 'cover',
    borderRadius: '12px',
    background: 'linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(139, 92, 246, 0.15) 100%)',
    padding: '0',
    boxShadow: '0 0 20px rgba(99, 102, 241, 0.4), 0 0 40px rgba(139, 92, 246, 0.2), inset 0 0 20px rgba(255, 255, 255, 0.05)',
    border: '1px solid rgba(139, 92, 246, 0.3)',
    transition: 'transform 0.3s cubic-bezier(0.4, 0, 0.2, 1)',
  },
  navBrandName: {
    fontSize: '19px',
    fontWeight: '700',
    color: '#fff',
    letterSpacing: '-0.3px',
  },
  navLinks: {
    position: 'absolute',
    left: '50%',
    transform: 'translateX(-50%)',
    display: 'flex',
    alignItems: 'center',
    gap: '2px',
    background: 'rgba(255, 255, 255, 0.03)',
    padding: '5px',
    borderRadius: '14px',
    border: '1px solid rgba(255, 255, 255, 0.04)',
  },
  navLink: {
    padding: '10px 20px',
    borderRadius: '10px',
    color: '#8892a6',
    fontSize: '14px',
    fontWeight: '500',
    cursor: 'pointer',
    transition: 'all 0.25s cubic-bezier(0.4, 0, 0.2, 1)',
    display: 'flex',
    alignItems: 'center',
    gap: '8px',
    position: 'relative',
  },
  navLinkActive: {
    background: 'rgba(255, 255, 255, 0.1)',
    color: '#fff',
  },
  navRight: {
    display: 'flex',
    alignItems: 'center',
    zIndex: 1,
  },
};

export default NavBar;
